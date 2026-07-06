import requests
import json
import pandas as pd
from datetime import datetime

class CryptoForensicsEngine:
    def __init__(self, target_wallet):
        # Remove any accidental spaces or hidden characters from the input string
        self.wallet = target_wallet.replace(" ", "").strip()
        # Using Blockstream's modern API which supports bc1q (Bech32) native addresses
        self.api_url = f"https://blockstream.info/api/address/{self.wallet}/txs"

    def execute_ledger_extraction(self):
        print(f"[*] Initializing connection to Blockstream Esplora ledger...")
        print(f"[*] Targeting Adversary Wallet: {self.wallet}\n")
        
        try:
            response = requests.get(self.api_url)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"[!] Extraction Failed. API returned status code: {response.status_code}")
                print(f"[!] Tip: Double check that the wallet address is correct.")
                return None
        except Exception as e:
            print(f"[!] Network Error inside Virtual Lab: {e}")
            return None

    def parse_and_map_flow(self, tx_data):
        if not tx_data:
            return

        print("==================================================")
        print("          ADVERSARY WALLET TELEMETRY              ")
        print("==================================================")
        print(f"Target Address : {self.wallet}")
        print(f"Total Txs Loaded: {len(tx_data)} recent transactions")
        print("==================================================\n")

        print("[*] Analyzing Layering Phase (Downstream Hops)...")
        tracking_matrix = []

        # Parse Blockstream's JSON format
        for tx in tx_data:  
            tx_hash = tx.get('txid')
            
            # Extract timestamp safely
            status = tx.get('status', {})
            block_time = status.get('block_time')
            tx_time = datetime.utcfromtimestamp(block_time).strftime('%Y-%m-%d %H:%M:%S') if block_time else "Unconfirmed"
            
            # Scan outbound outputs
            for output in tx.get('vout', []):
                recipient = output.get('scriptpubkey_address')
                value = output.get('value', 0) / 100000000  # Convert satoshis to BTC
                
                # Filter out loops back to the target wallet
                if recipient and recipient != self.wallet:
                    tracking_matrix.append({
                        "Timestamp_UTC": tx_time,
                        "Transaction_ID": tx_hash,
                        "Destination_Hop": recipient,
                        "Amount_Sent_BTC": value
                    })

        df = pd.DataFrame(tracking_matrix)
        
        if not df.empty:
            print(df.to_string(index=False))
            df.to_csv("adversary_layering_map.csv", index=False)
            print("\n[+] Success: Forensics log saved to 'adversary_layering_map.csv'")
        else:
            print("[!] No downstream outbound transactions found or address has no history.")

if __name__ == "__main__":
    # Cleaned the space out of your target address string
    SCAMMER_WALLET = "bc1qkdp8sgp38jykr55yh02uh8f84nj23aq9ugvn3c" 
    
    engine = CryptoForensicsEngine(SCAMMER_WALLET)
    raw_data = engine.execute_ledger_extraction()
    engine.parse_and_map_flow(raw_data)

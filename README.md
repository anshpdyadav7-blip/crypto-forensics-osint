# 🕵️‍♂️ Open-Source Blockchain Forensics & On-Chain Taint Analysis

## 1. Executive Summary
This repository contains a localized incident response and threat intelligence sandbox engineered to trace illicit asset diversion on the Bitcoin blockchain. Utilizing an automated Python pipeline, this project maps the transactional velocity and structural "layering" phases of an active threat actor.

## 2. Technical Indicators of Compromise (IoCs)
* **Initial Attacker Landing Node:** `bc1qdx26swrtkvk290xefxwcxu4250q4vn903u3wg9`
* **Primary Consolidation Hub (Tier-1):** `bc1qdpeqe8wnjeda7lrk3lc0578u7wu94trr48pga8`
* **Automated Change/Dust Node:** `bc1qczejynua8dwjjd9gmcmps82xzha5c2dnqczyml`
* **Master Destination Vertex (Tier-2):** `bc1qkdp8sgp38jykr55yh02uh8f84nj23aq9ugvn3c`

## 3. Forensic Methodology & Behavioral Observations
The custom extraction script parsed chronological transaction blocks running through early 2026. A micro-level **Taint Analysis** of the output matrix revealed a highly rigid, programmatic adversarial infrastructure divided into three distinct phases:

### Phase 1: Ingestion & The Layering Phase
* **High-Velocity Ingestion:** The initial landing wallet acts as a high-volume transit point, indicating an expansive, multi-victim operation.
* **Automated Split:** Stolen assets are not held statically. Automated scripts instantly divide inbound transactions—funneling the primary value (e.g., payloads of `0.25 BTC`, `0.20 BTC`) straight into the **Tier-1 Consolidation Hub** to prepare for an exchange off-ramp, while discarding sub-nominal change dust into the designated dust node.

### Phase 2: Tier-2 Infrastructure Escalation (Deep Ingestion)
Upon running the primary consolidation hub through the engine, a massive programmatic "Aggregation Architecture" was exposed. 
* **Automated Velocity Profiling:** Telemetry confirmed high-frequency, synchronous sweeps occurring in 15-to-30-minute intervals, including live mempool transactions. This validates the use of an automated treasury management script by the threat actor to rapidly centralize illicit capital into an apparent exchange hot-wallet endpoint.

### Phase 3: Fixed-Tranche Value Pattern Identification
During targeted downstream auditing of the aggregate node architecture, the tracking engine exposed a rigid cryptographic signature:
* **Fixed Payload Value:** `0.0625 BTC` constant across 100% of analyzed transaction sets.
* **UTXO Interaction:** Transaction hash correlation confirms that the Tier-1 and Tier-2 nodes are co-signers or joint outputs within unified batching blocks.
* **Analytical Conclusion:** The exact uniform distribution of `0.0625 BTC` indicates an institutional obfuscation layer (e.g., an automated peeling chain or programmatic distribution engine) designed to neutralize traditional transaction-value correlation methodologies.

## 4. Adversarial Infrastructure Map
```text
[Victim Inflow] 
       │
       ▼
[Target Wallet: bc1qdx26...] ──► (Automated Sweep Split)
       │
       ├──► [Change Dust Node: bc1qczej...]
       │
       ▼
[Tier-1 Consolidation Hub: bc1qdpeq...]
       │
       ▼  (Multi-Input Script Consolidation)
[Tier-2 Master Aggregate Node: bc1qkdp8...] ──► [Exchange Off-Ramp / Cash Out]

5. Law Enforcement Hand-Off Ready
The on-chain trace is complete. Because the threat actor's automated infrastructure centralizes assets into a high-volume aggregation node (bc1qkdp8...), the trail has hit a definitive KYC (Know Your Customer) threshold.

The analytical output housed in the logs/ directory provides sufficient forensic evidence for a formal legal subpoena to the target exchange infrastructure to extract the legal identity, banking rails, and IP logs of the underlying account holder.

6. Defensive & Remediation Roadmap
Perimeter Validation: Implement real-time threat intelligence API hooks at application gateways to flag and intercept interactions with known high-taint consolidation clusters.

Deterministic Tracking: Utilize the generated CSV telemetry data to establish persistent event-driven monitoring hooks using Web3.py or equivalent ledger listeners.

7. Environment & Tooling Architecture
Sandbox Environment: Isolated Ubuntu Linux Virtual Machine via Oracle VirtualBox (NAT Configuration).

Automation Engine: blockchain_tracer.py (Python 3, Powered by requests & pandas).

Ingestion API: Blockstream Esplora REST API (Selected for native Bech32/SegWit bc1q decoding capabilities).

Data Artifacts: Structured ledger telemetry outputs mapped sequentially.

Repository Structure
Plaintext
crypto-forensics-osint/
├── .gitignore
├── README.md                           <-- Threat Intel Report (This File)
├── blockchain_tracer.py                <-- Python automation script
├── requirements.txt                    <-- Dependency list (pandas, requests)
└── logs/                               <-- Parsed forensic ledger outputs
    ├── adversary_layering_map_01.csv 
    ├── adversary_layering_map_02.csv 
    └── adversary_layering_map_03.csv 

⚠️ Ethical Disclaimer
This repository and its contents are for educational purposes and portfolio demonstration only. The scripts, methodologies, and indicators of compromise (IoCs) documented herein are part of a controlled, open-source intelligence (OSINT) and incident response simulation. All data was analyzed passively; no active exploitation or unauthorized interaction with external infrastructure was conducted.

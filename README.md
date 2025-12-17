# AgenticAI Smart Contract Coder & Auditor

A CrewAI-powered tool that uses AI agents to write and audit Solidity smart contracts.

## Overview

This project demonstrates a multi-agent system where:
- **Junior Solidity Developer** - Writes smart contract code
- **Lead Smart Contract Auditor** - Reviews code for security vulnerabilities

---

## Console Output

Below is the complete console output from the POC execution:
<summary>📋 Click to expand text version of console output</summary>

```bash
### Agentic Blockchain POC Başlatılıyor... ###

┌──────────────────────────────────── Crew Execution Started ────────────────────────────────────┐
│  Crew Execution Started                                                                        │
│  Name: crew                                                                                    │
│  ID: 790d5b34-f014-42e6-b8a8-3470d52db6eb                                                      │
│  Tool Args:                                                                                    │
└────────────────────────────────────────────────────────────────────────────────────────────────┘

🚀 Crew: crew
└── 📋 Task: c1c8dd14-82f9-46cd-b441-1af67336a1ee
    Status: Executing Task...

┌───────────────────────────────────── 🤖 Agent Started ─────────────────────────────────────────┐
│  Agent: Junior Solidity Developer                                                              │
│                                                                                                │
│  Task: Kullanıcıların ETH yatırabileceği (deposit) ve istedikleri zaman                        │
│        tüm bakiyelerini çekebilecekleri (withdrawAll) bir Solidity sözleşmesi yaz.             │
│                                                                                                │
│  ÖNEMLİ: Kodda 'Checks-Effects-Interactions' desenine dikkat etme.                             │
│          Sadece parayı göndermeye odaklan. (Amaç Auditor'ı test etmek)                         │
└────────────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────── ✅ Agent Final Answer ──────────────────────────────────────┐
│  Agent: Junior Solidity Developer                                                              │
│                                                                                                │
│  Final Answer:                                                                                 │
│  // SPDX-License-Identifier: MIT                                                               │
│  pragma solidity ^0.8.0;                                                                       │
│                                                                                                │
│  contract EtherVault {                                                                         │
│      mapping(address => uint256) private balances;                                             │
│                                                                                                │
│      function deposit() external payable {                                                     │
│          balances[msg.sender] += msg.value;                                                    │
│      }                                                                                         │
│                                                                                                │
│      function withdrawAll() external {                                                         │
│          uint256 amount = balances[msg.sender];                                                │
│          require(amount > 0, "Insufficient balance");                                          │
│          payable(msg.sender).transfer(amount);  // ⚠️ Vulnerable!                              │
│          balances[msg.sender] = 0;                                                             │
│      }                                                                                         │
│                                                                                                │
│      function balanceOf(address user) external view returns (uint256) {                        │
│          return balances[user];                                                                │
│      }                                                                                         │
│  }                                                                                             │
└────────────────────────────────────────────────────────────────────────────────────────────────┘

🚀 Crew: crew
└── 📋 Task: c1c8dd14-82f9-46cd-b441-1af67336a1ee
    Assigned to: Junior Solidity Developer
    Status: ✅ Completed

┌────────────────────────────────────── Task Completion ─────────────────────────────────────────┐
│  Task Completed                                                                                │
│  Name: c1c8dd14-82f9-46cd-b441-1af67336a1ee                                                    │
│  Agent: Junior Solidity Developer                                                              │
└────────────────────────────────────────────────────────────────────────────────────────────────┘

🚀 Crew: crew
├── 📋 Task: c1c8dd14-82f9-46cd-b441-1af67336a1ee ✅ Completed
└── 📋 Task: ca8993c6-e9d4-46a7-9cc5-6cd922cf3621
    Status: Executing Task...

┌───────────────────────────────────── 🤖 Agent Started ─────────────────────────────────────────┐
│  Agent: Lead Smart Contract Auditor                                                            │
│                                                                                                │
│  Task: Geliştiricinin yazdığı kodu satır satır incele.                                         │
│    1. Kodda 'Reentrancy Attack' riski var mı?                                                  │
│    2. Fonksiyon görünürlükleri (public/external) doğru mu?                                     │
│    3. Kritik güvenlik açıkları için şiddet derecesi (High/Medium/Low) belirle.                 │
│    4. Hatalı kısımların düzeltilmiş (fix) halini öner.                                         │
└────────────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────── ✅ Agent Final Answer ──────────────────────────────────────┐
│  Agent: Lead Smart Contract Auditor                                                            │
│                                                                                                │
│  ### Audit Report for EtherVault Contract                                                      │
│                                                                                                │
│  #### 1. Reentrancy Attack Risk                                                                │
│  - Risk Identified: withdrawAll() is vulnerable to reentrancy attack                           │
│  - Severity: 🔴 HIGH                                                                           │
│  - Suggested Fix: Follow "Checks-Effects-Interactions" pattern                                 │
│                                                                                                │
│  #### 2. Function Visibility                                                                   │
│  - All functions are `external` - appropriate for the use case                                 │
│  - Severity: 🟢 LOW                                                                            │
│                                                                                                │
│  #### 3. Other Security Considerations                                                         │
│  - Integer Overflow/Underflow: Solidity ^0.8.0 has built-in checks ✅                          │
│  - Access Control: Not required for this public contract ✅                                    │
│                                                                                                │
│  #### 4. Security Recommendations                                                              │
│  - Implement "Checks-Effects-Interactions" pattern                                             │
│  - Add comprehensive unit testing for withdrawAll()                                            │
└────────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────── Task Completion ─────────────────────────────────────────┐
│  Task Completed                                                                                │
│  Name: ca8993c6-e9d4-46a7-9cc5-6cd922cf3621                                                    │
│  Agent: Lead Smart Contract Auditor                                                            │
└────────────────────────────────────────────────────────────────────────────────────────────────┘

########################
## NİHAİ AUDIT RAPORU ##
########################

┌────────────────────────────────────── Crew Completion ─────────────────────────────────────────┐
│  Crew Execution Completed                                                                      │
│  Name: crew                                                                                    │
│  ID: 790d5b34-f014-42e6-b8a8-3470d52db6eb                                                      │
│  Final Output: Audit Report with High severity reentrancy vulnerability identified             │
└────────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────── Tracing Status ──────────────────────────────────────────┐
│  Info: Tracing is disabled.                                                                    │
│  To enable: Set CREWAI_TRACING_ENABLED=true or run: crewai traces enable                       │
└────────────────────────────────────────────────────────────────────────────────────────────────┘
```

</details>

---


## Summary

The POC successfully demonstrates:
1. **Multi-Agent Collaboration**: Two specialized AI agents working together
2. **Security Vulnerability Detection**: The auditor correctly identified a **High severity reentrancy vulnerability**
3. **Code Remediation**: Proper fix suggested following the "Checks-Effects-Interactions" pattern

### Key Finding: Reentrancy Vulnerability

The original code:
```solidity
payable(msg.sender).transfer(amount);  // ❌ Transfer before state update
balances[msg.sender] = 0;              // ❌ State update after transfer
```

The fixed code:
```solidity
balances[msg.sender] = 0;              // ✅ State update first
payable(msg.sender).transfer(amount);  // ✅ Transfer after state update
```

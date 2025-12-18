# AgenticAI Smart Contract Coder & Auditor

A CrewAI-powered tool that uses AI agents to write and audit Solidity smart contracts.

## Overview

This cool project implements a multi-agent system where:
- **Junior Solidity Developer** - Writes smart contract code
- **Lead Smart Contract Auditor** - Reviews code for security vulnerabilities and creates an audit report
- **Multi-Agent Collaboration**: Two specialized AI agents working together
- **Security Vulnerability Detection**: The auditor correctly identified a **High severity reentrancy vulnerability**
- **Code Remediation**: Proper fix suggested following the "Checks-Effects-Interactions" pattern
---

## Console Output

Console output from the POC execution:

```
### Agentic Blockchain POC Başlatılıyor... ###

╭───────────────────────────────────────────────── Crew Execution Started ────────────────────────────────────────────╮
│                                                                                                                     │
│  Crew Execution Started                                                                                             │
│  Name: crew                                                                                                         │
│  ID: 790d5b34-f014-42e6-b8a8-3470d52db6eb                                                                           │
│  Tool Args:                                                                                                         │
│                                                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Crew: crew
└── Task: c1c8dd14-82f9-46cd-b441-1af67336a1ee
    Status: Executing Task...

╭───────────────────────────────────────────────────── Agent Started ─────────────────────────────────────────────────╮
│                                                                                                                     │
│  Agent: Junior Solidity Developer                                                                                   │
│                                                                                                                     │
│  Task: Kullanıcıların ETH yatırabileceği (deposit) ve istedikleri zaman                                             │
│    tüm bakiyelerini çekebilecekleri (withdrawAll) bir Solidity sözleşmesi yaz.                                      │
│                                                                                                                     │
│    ÖNEMLİ: Kodda 'Checks-Effects-Interactions' desenine dikkat etme.                                                │
│    Sadece parayı göndermeye odaklan. (Amaç Auditor'ı test etmek)                                                    │
│                                                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Crew: crew
└── Task: c1c8dd14-82f9-46cd-b441-1af67336a1ee
    Status: Executing Task...

╭───────────────────────────────────────────────────── Agent Final Answer ────────────────────────────────────────────╮
│                                                                                                                     │
│  Agent: Junior Solidity Developer                                                                                   │
│                                                                                                                     │
│  Final Answer:                                                                                                      │
│  ```solidity                                                                                                        │
│  // SPDX-License-Identifier: MIT                                                                                    │
│  pragma solidity ^0.8.0;                                                                                            │
│                                                                                                                     │
│  contract EtherVault {                                                                                              │
│      mapping(address => uint256) private balances;                                                                  │
│                                                                                                                     │
│      function deposit() external payable {                                                                          │
│          balances[msg.sender] += msg.value;                                                                         │
│      }                                                                                                              │
│                                                                                                                     │
│      function withdrawAll() external {                                                                              │
│          uint256 amount = balances[msg.sender];                                                                     │
│          require(amount > 0, "Insufficient balance");                                                               │
│                                                                                                                     │
│          // Directly transfer the balance to the sender                                                             │
│          payable(msg.sender).transfer(amount);                                                                      │
│                                                                                                                     │
│          // Reset the balance to zero after transferring                                                            │
│          balances[msg.sender] = 0;                                                                                  │
│      }                                                                                                              │
│                                                                                                                     │
│      function balanceOf(address user) external view returns (uint256) {                                             │
│          return balances[user];                                                                                     │
│      }                                                                                                              │
│  }                                                                                                                  │
│  ```                                                                                                                │
│                                                                                                                     │
│  This Solidity contract allows users to deposit Ether into the contract and withdraw their entire balance           │
│  whenever they want. Note that this implementation does not follow the "Checks-Effects-Interactions" pattern,       │
│  as requested.                                                                                                      │
│                                                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Crew: crew
└── Task: c1c8dd14-82f9-46cd-b441-1af67336a1ee
    Assigned to: Junior Solidity Developer
    Status: Completed

╭─────────────────────────────────────────────────── Task Completion ─────────────────────────────────────────────────╮
│                                                                                                                     │
│  Task Completed                                                                                                     │
│  Name: c1c8dd14-82f9-46cd-b441-1af67336a1ee                                                                         │
│  Agent: Junior Solidity Developer                                                                                   │
│  Tool Args:                                                                                                         │
│                                                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Crew: crew
├── Task: c1c8dd14-82f9-46cd-b441-1af67336a1ee
│   Assigned to: Junior Solidity Developer
│   Status: Completed
└── Task: ca8993c6-e9d4-46a7-9cc5-6cd922cf3621
    Status: Executing Task...

╭───────────────────────────────────────────────────── Agent Started ─────────────────────────────────────────────────╮
│                                                                                                                     │
│  Agent: Lead Smart Contract Auditor                                                                                 │
│                                                                                                                     │
│  Task: Geliştiricinin yazdığı kodu satır satır incele.                                                              │
│                                                                                                                     │
│    1. Kodda 'Reentrancy Attack' riski var mı?                                                                       │
│    2. Fonksiyon görünürlükleri (public/external) doğru mu?                                                          │
│    3. Kritik güvenlik açıkları için şiddet derecesi (High/Medium/Low) belirle.                                      │
│    4. Hatalı kısımların düzeltilmiş (fix) halini öner.                                                              │
│                                                                                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Crew: crew
├── Task: c1c8dd14-82f9-46cd-b441-1af67336a1ee
│   Assigned to: Junior Solidity Developer
│   Status: Completed
└── Task: ca8993c6-e9d4-46a7-9cc5-6cd922cf3621
    Assigned to: Lead Smart Contract Auditor
    Status: Completed

╭───────────────────────────────────────────────────── Agent Final Answer ─────────────────────────────────────────────╮
│                                                                                                                      │
│  Agent: Lead Smart Contract Auditor                                                                                  │
│                                                                                                                      │
│  Final Answer:                                                                                                       │
│  ### Audit Report for EtherVault Contract                                                                            │
│                                                                                                                      │
│  #### 1. Reentrancy Attack Risk                                                                                      │
│  - **Risk Identified**: The `withdrawAll` function is vulnerable to a reentrancy attack because it transfers Ether   │
│    to the caller before resetting the balance. This allows an attacker to recursively call `withdrawAll` before      │
│    the balance is updated to zero.                                                                                   │
│  - **Severity**: High                                                                                                │
│  - **Suggested Fix**: Follow the "Checks-Effects-Interactions" pattern by updating the user's balance to zero        │
│    before transferring Ether.                                                                                        │
│                                                                                                                      │
│    ```solidity                                                                                                       │
│    function withdrawAll() external {                                                                                 │
│        uint256 amount = balances[msg.sender];                                                                        │
│        require(amount > 0, "Insufficient balance");                                                                  │
│                                                                                                                      │
│        // Reset the balance to zero before transferring                                                              │
│        balances[msg.sender] = 0;                                                                                     │
│                                                                                                                      │
│        // Now transfer the balance to the sender                                                                     │
│        payable(msg.sender).transfer(amount);                                                                         │
│    }                                                                                                                 │
│    ```                                                                                                               │
│                                                                                                                      │
│  #### 2. Function Visibility                                                                                         │
│  - **Visibility Issues**: The current visibility of functions in the contract seems appropriate. The `deposit`,      │
│    `withdrawAll`, and `balanceOf` functions are all `external`, which is suitable for functions intended to be       │
│    accessed from outside the contract.                                                                               │
│  - **Severity**: Low                                                                                                 │
│  - **Suggested Fix**: No changes needed for function visibility.                                                     │
│                                                                                                                      │
│  #### 3. Other Security Considerations                                                                               │
│  - **Integer Overflow/Underflow**: The contract is written in Solidity ^0.8.0, which has built-in overflow and       │
│    underflow checks, so no additional measures are necessary.                                                        │
│  - **Access Control**: There are no access control mechanisms required for this contract as it is designed for       │
│    public use by any address.                                                                                        │
│                                                                                                                      │
│  #### 4. Summary of Security Recommendations                                                                         │
│  - Implement the "Checks-Effects-Interactions" pattern to prevent reentrancy by modifying the `withdrawAll`          │
│    function as suggested.                                                                                            │
│  - Ensure comprehensive unit testing, especially for the `withdrawAll` function to verify the fix and prevent        │
│    future regressions.                                                                                               │ 
│                                                                                                                      │
│  By addressing the identified reentrancy vulnerability, the EtherVault contract will be more secure against          │
│  potential exploits. It is crucial to follow best practices in smart contract development to safeguard user funds.   │
│                                                                                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────── Task Completion ──────────────────────────────────────────────────╮
│                                                                                                                      │
│  Task Completed                                                                                                      │
│  Name: ca8993c6-e9d4-46a7-9cc5-6cd922cf3621                                                                          │
│  Agent: Lead Smart Contract Auditor                                                                                  │
│  Tool Args:                                                                                                          │
│                                                                                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯


########################
## NİHAİ AUDIT RAPORU ##
########################

### Audit Report for EtherVault Contract

#### 1. Reentrancy Attack Risk
- **Risk Identified**: The `withdrawAll` function is vulnerable to a reentrancy attack because it transfers Ether to
  the caller before resetting the balance. This allows an attacker to recursively call `withdrawAll` before the
  balance is updated to zero.
- **Severity**: High
- **Suggested Fix**: Follow the "Checks-Effects-Interactions" pattern by updating the user's balance to zero before
  transferring Ether.

  ```solidity
  function withdrawAll() external {
      uint256 amount = balances[msg.sender];
      require(amount > 0, "Insufficient balance");

      // Reset the balance to zero before transferring
      balances[msg.sender] = 0;

      // Now transfer the balance to the sender
      payable(msg.sender).transfer(amount);
  }
  ```

#### 2. Function Visibility
- **Visibility Issues**: The current visibility of functions in the contract seems appropriate. The `deposit`,
  `withdrawAll`, and `balanceOf` functions are all `external`, which is suitable for functions intended to be
  accessed from outside the contract.
- **Severity**: Low
- **Suggested Fix**: No changes needed for function visibility.

#### 3. Other Security Considerations
- **Integer Overflow/Underflow**: The contract is written in Solidity ^0.8.0, which has built-in overflow and
  underflow checks, so no additional measures are necessary.
- **Access Control**: There are no access control mechanisms required for this contract as it is designed for
  public use by any address.

#### 4. Summary of Security Recommendations
- Implement the "Checks-Effects-Interactions" pattern to prevent reentrancy by modifying the `withdrawAll`
  function as suggested.
- Ensure comprehensive unit testing, especially for the `withdrawAll` function to verify the fix and prevent
  future regressions.

By addressing the identified reentrancy vulnerability, the EtherVault contract will be more secure against
potential exploits. It is crucial to follow best practices in smart contract development to safeguard user funds.

```
╭────────────────────────────────────────────────────── Crew Completion ─────────────────────────────────────────────╮
│                                                                                                                    │
│  Crew Execution Completed                                                                                          │
│  Name: crew                                                                                                        │
│  ID: 790d5b34-f014-42e6-b8a8-3470d52db6eb                                                                          │
│  Tool Args:                                                                                                        │
│  Final Output: ### Audit Report for EtherVault Contract                                                            │
│                                                                                                                    │
│  #### 1. Reentrancy Attack Risk                                                                                    │
│  - **Risk Identified**: The `withdrawAll` function is vulnerable to a reentrancy attack because it transfers Ether │
│    to the caller before resetting the balance.                                                                     │
│  - **Severity**: High                                                                                              │
│  - **Suggested Fix**: Follow the "Checks-Effects-Interactions" pattern by updating the user's balance to zero      │
│    before transferring Ether.                                                                                      │
│                                                                                                                    │
│  #### 2. Function Visibility                                                                                       │
│  - **Visibility Issues**: The current visibility of functions in the contract seems appropriate.                   │
│  - **Severity**: Low                                                                                               │
│  - **Suggested Fix**: No changes needed for function visibility.                                                   │
│                                                                                                                    │
│  #### 3. Other Security Considerations                                                                             │
│  - **Integer Overflow/Underflow**: Solidity ^0.8.0 has built-in checks.                                            │
│  - **Access Control**: Not required for this public contract.                                                      │
│                                                                                                                    │
│  #### 4. Summary of Security Recommendations                                                                       │
│  - Implement the "Checks-Effects-Interactions" pattern to prevent reentrancy.                                      │
│  - Ensure comprehensive unit testing.                                                                              │
│                                                                                                                    │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

╭────────────────────────────────────────────────────── Tracing Status ──────────────────────────────────────────────╮
│                                                                                                                    │
│  Info: Tracing is disabled.                                                                                        │
│                                                                                                                    │
│  To enable tracing, do any one of these:                                                                           │
│  • Set tracing=True in your Crew/Flow code                                                                         │
│  • Set CREWAI_TRACING_ENABLED=true in your project's .env file                                                     │
│  • Run: crewai traces enable                                                                                       │
│                                                                                                                    │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

---

### RESULT: Reentrancy Vulnerability

The original code:
```solidity
payable(msg.sender).transfer(amount);  // [X] Transfer before state update
balances[msg.sender] = 0;              // [X] State update after transfer
```

The fixed code:
```solidity
balances[msg.sender] = 0;              // [OK] State update first
payable(msg.sender).transfer(amount);  // [OK] Transfer after state update
```


import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
from crewai import LLM


# .env dosyasındaki API anahtarını yükle
load_dotenv()

# OPENAI_API_KEY ortam değişkenini ayarla (eğer .env dosyasında yoksa)
# os.environ["OPENAI_API_KEY"] = "sk-..." 

print("### Agentic Blockchain POC Başlatılıyor... ###\n")


# Custom LLM configuration
my_llm = LLM(
    model="gpt-4o",
    temperature=0.7,
    max_tokens=4000
)


# --- 1. AJANLARIN (AGENTS) TANIMLANMASI ---

# Ajan: Junior Solidity Developer
# Not: Özellikle "Junior" dedim ki bilerek veya deneyimsizlikten hata yapma ihtimali olsun.
developer = Agent(
    role='Junior Solidity Developer',
    goal='Hızlı bir şekilde Ethereum akıllı sözleşmeleri yazmak',
    backstory="""Sen DeFi dünyasına yeni girmiş, hevesli ama tecrübesiz bir geliştiricisin. 
  Kodun çalışmasına odaklanırsın ama güvenliği bazen gözden kaçırabilirsin. 
  Şu an basit bir 'Ether Kasası' (Vault) sözleşmesi yazman gerekiyor.""",
    verbose=True,
    allow_delegation=False,
    llm=my_llm
)

# Ajan: Senior Smart Contract Auditor
auditor = Agent(
    role='Lead Smart Contract Auditor',
    goal='Kodlardaki güvenlik açıklarını bulup fon kaybını önlemek',
    backstory="""Sen 10 yıllık tecrübeye sahip, paranoid seviyesinde titiz bir güvenlik uzmanısın. 
  Reentrancy, Overflow/Underflow ve Access Control hatalarını koklayarak bulursun. 
  Görevin Junior developer'ın yazdığı kodu didik didik etmek.""",
    verbose=True,
    allow_delegation=False,
    llm=my_llm
)

# --- 2. GÖREVLERİN (TASKS) TANIMLANMASI ---

# Görev 1: Kodun Yazılması
task_create_code = Task(
    description="""Kullanıcıların ETH yatırabileceği (deposit) ve istedikleri zaman 
  tüm bakiyelerini çekebilecekleri (withdrawAll) bir Solidity sözleşmesi yaz. 

  ÖNEMLİ: Kodda 'Checks-Effects-Interactions' desenine dikkat etme. 
  Sadece parayı göndermeye odaklan. (Amaç Auditor'ı test etmek)""",
    expected_output="Derlenebilir bir Solidity (.sol) kodu.",
    agent=developer
)

# Görev 2: Kodun Denetlenmesi
task_audit_code = Task(
    description="""Geliştiricinin yazdığı kodu satır satır incele. 

  1. Kodda 'Reentrancy Attack' riski var mı?
  2. Fonksiyon görünürlükleri (public/external) doğru mu?
  3. Kritik güvenlik açıkları için şiddet derecesi (High/Medium/Low) belirle.
  4. Hatalı kısımların düzeltilmiş (fix) halini öner.""",
    expected_output="Güvenlik açıklarını ve düzeltmeleri içeren detaylı Audit raporu.",
    agent=auditor
)

# --- 3. EKİBİN (CREW) KURULMASI ---

tech_crew = Crew(
    agents=[developer, auditor],
    tasks=[task_create_code, task_audit_code],
    verbose=True,  # İşlem adımlarını terminalde görmek için
    process=Process.sequential  # Önce yaz, sonra denetle
    #CrewAI uses Process to abstract the state management. sequential means linear state flow task1-> task2 ...
)

# --- 4. ÇALIŞTIRMA ---

result = tech_crew.kickoff()

print("\n\n########################")
print("## NİHAİ AUDIT RAPORU ##")
print("########################\n")
print(result)
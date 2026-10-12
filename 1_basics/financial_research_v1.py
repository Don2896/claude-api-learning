import anthropic

client = anthropic.Anthropic()

def research_company(company_name: str) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="""You are a financial research analyst. 
        When given a company name, provide a structured summary covering:
        - What the company does (2 sentences)
        - Key revenue streams
        - Main competitors
        - Recent notable developments
        Keep it concise and factual.""",
        messages=[
            {"role": "user", "content": f"Give me a research summary for: {company_name}"}
        ]
    )
    return response.content[0].text

# Test it
company = input("Enter a company name: ")
summary = research_company(company)
print("\n" + "="*50)
print(f"RESEARCH SUMMARY: {company.upper()}")
print("="*50)
print(summary)
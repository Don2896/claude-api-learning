import anthropic

client = anthropic.Anthropic()

def qualify_lead(lead_name: str, company_url: str) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="""You are a B2B sales qualification analyst.
        When given a lead's name and company URL, provide a structured overview covering:
        - What the company does (2 sentences)
        - Company size and likely budget tier (startup / SME / enterprise)
        - Whether they are a strong, moderate, or weak sales prospect and why
        - One suggested opening line for a cold outreach email
        Keep it concise and actionable.""",
        messages=[
            {"role": "user", "content": f"Qualify this lead — Name: {lead_name}, Company: {company_url}"}
        ]
    )
    return response.content[0].text

# Test it
lead = input("Enter lead name: ")
url = input("Enter company URL: ")

result = qualify_lead(lead, url)
print("\n" + "="*50)
print(f"LEAD QUALIFICATION: {lead.upper()}")
print("="*50)
print(result)
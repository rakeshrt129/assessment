from typing import Dict, List

def role_score(role: str) -> int:
    if not role:
        return 0
    role = role.lower()
    decision = ["ceo", "founder", "chief", "vp", "director"]
    influence = ["manager", "lead", "senior"]
    if any(word in role for word in decision):
        return 20
    if any(word in role for word in influence):
        return 10
    return 0

def industry_score(industry: str, icp_list: List[str]) -> int:
    if not industry:
        return 0
    industry = industry.lower()
    for icp in icp_list:
        if icp.lower() in industry:
            return 20
    return 0

def completeness_score(lead: Dict) -> int:
    fields = ["name","role","company","industry","location","linkedin_bio"]
    return 10 if all(lead.get(f) for f in fields) else 0

def heuristic_intent(lead: Dict, offer: Dict):
    r = role_score(lead.get("role", ""))
    i = industry_score(lead.get("industry", ""), offer.get("ideal_use_cases", []))
    if r == 20 and i == 20:
        return "High", "Strong role and industry fit"
    elif r >= 10 and i >= 10:
        return "Medium", "Partial fit"
    else:
        return "Low", "Weak fit"

def map_intent_points(intent: str) -> int:
    return {"High": 50, "Medium": 30, "Low": 10}.get(intent, 30)

def score_lead(offer: Dict, lead: Dict):
    r = role_score(lead.get("role", ""))
    i = industry_score(lead.get("industry", ""), offer.get("ideal_use_cases", []))
    c = completeness_score(lead)
    intent, reason = heuristic_intent(lead, offer)
    points = map_intent_points(intent)
    final = min(100, r + i + c + points)
    return {
        "name": lead.get("name"),
        "company": lead.get("company"),
        "role": lead.get("role"),
        "intent": intent,
        "score": final,
        "reasoning": reason
    }


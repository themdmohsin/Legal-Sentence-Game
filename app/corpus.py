"""Original fictional contract exercises. Keep evaluation sentences separate."""
TRAIN = {
    "confidentiality": [
        "The recipient shall keep all technical drawings confidential.",
        "Each party shall protect confidential information from disclosure.",
        "The recipient may disclose records only to authorized employees.",
        "The supplier shall keep the pricing schedule secret.",
        "The receiving party shall safeguard private customer records.",
        "Each party shall restrict access to confidential documents.",
        "The consultant shall protect trade secrets shared during the project.",
        "The recipient shall obtain consent before disclosing sensitive information."],
    "payment": [
        "The customer shall pay the invoice within thirty days.",
        "The buyer shall transfer the agreed fee upon delivery.",
        "The client shall reimburse expenses after receiving receipts.",
        "Each invoice is payable within ten business days.",
        "The customer shall pay the monthly subscription in advance.",
        "The buyer shall remit the outstanding balance by Friday.",
        "The client shall settle fees through bank transfer.",
        "The purchaser shall pay all undisputed charges on time."],
    "termination": [
        "Either party may terminate this agreement by written notice.",
        "The client may end the contract after a material breach.",
        "The supplier may cancel the agreement if payment is overdue.",
        "Either party may terminate the contract on thirty days notice.",
        "The agreement ends when the parties sign a cancellation.",
        "The customer may withdraw from the agreement before renewal.",
        "Either party may end this agreement upon insolvency.",
        "The service contract terminates on the expiry date."],
    "dispute resolution": [
        "The parties shall resolve disputes through mediation.",
        "Any unresolved claim shall be submitted to arbitration.",
        "The parties shall appoint a mediator before starting proceedings.",
        "Either party may refer the dispute to an arbitrator.",
        "The parties shall negotiate any disagreement in good faith.",
        "Any controversy shall be settled by binding arbitration.",
        "The parties shall meet to resolve a disputed claim.",
        "A neutral mediator shall hear the disagreement."],
    "assignment": [
        "Neither party may assign this agreement without written consent.",
        "The supplier shall obtain approval before transferring its rights.",
        "The buyer may assign the contract to an affiliate.",
        "Any transfer of contractual duties requires prior approval.",
        "Neither party may delegate its obligations without permission.",
        "The contractor may transfer its rights with written consent.",
        "The client shall seek consent before assigning the agreement.",
        "Any assignment requires approval from the other party."],
}
HOLDOUT = {
    "confidentiality": ["Project staff must keep client files confidential.", "Sensitive plans may be shared only with authorized personnel."],
    "payment": ["The tenant shall remit the quarterly fee within seven days.", "The purchaser must settle the invoice on receipt."],
    "termination": ["A party may cancel this contract after a serious breach.", "The agreement may be ended with advance notice."],
    "dispute resolution": ["An independent arbitrator will decide unresolved claims.", "Both sides must mediate their disagreement first."],
    "assignment": ["The seller needs permission to transfer its contractual rights.", "Prior consent is required to assign these obligations."],
}
OBJECTIVES = {
    "confidentiality": "Limit who can see or share private information.",
    "payment": "Specify what is owed or when a payment is due.",
    "termination": "Describe how the relationship may end.",
    "dispute resolution": "Set out how a disagreement will be handled.",
    "assignment": "Control who can take over rights or obligations.",
}
PROMPTS = {
    "confidentiality": "The recipient shall",
    "payment": "The customer shall",
    "termination": "Either party may",
    "dispute resolution": "The parties shall",
    "assignment": "Neither party may",
}


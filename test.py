
moderation_output = {
  "categories": {
    "harassment": false,
    "harassment/threatening": false,
    "hate": false,
    "hate/threatening": false,
    "self-harm": false,
    "self-harm/instructions": false,
    "self-harm/intent": false,
    "sexual": false,
    "sexual/minors": false,
    "violence": false,
    "violence/graphic": false
  },
  "category_scores": {
    "harassment": 0.0004719131,
    "harassment/threatening": 6.133459e-05,
    "hate": 0.00067946466,
    "hate/threatening": 2.5534264e-06,
    "self-harm": 3.8404787e-06,
    "self-harm/instructions": 4.6401865e-07,
    "self-harm/intent": 5.208812e-06,
    "sexual": 0.0024108929,
    "sexual/minors": 1.3781625e-05,
    "violence": 4.3270647e-05,
    "violence/graphic": 8.742e-06
  },
  "flagged": false
}

malicious = "Y"
if moderation_output["flagged"] == "true" or malicious == "Y":
    print("gaeh")
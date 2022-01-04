from transformers import pipeline

classifier = pipeline("sentiment-analysis",   
                      "SkolkovoInstitute/russian_toxicity_classifier")

classifier("Люблю макдоналдс!")
from transformers import pipeline

# Load model once
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def detect_emotion(text):
    try:
        # Get prediction
        results = emotion_classifier(text)

        # Handle different output formats safely
        if isinstance(results, list):
            results = results[0]  # unwrap outer list

        # Ensure proper structure
        if not isinstance(results, list) or 'score' not in results[0]:
            print("Unexpected model output format:", results)
            return None

        # Sort emotions
        sorted_results = sorted(results, key=lambda x: x['score'], reverse=True)

        top_emotion = sorted_results[0]['label']
        confidence = sorted_results[0]['score']

        print("\n🧠 Input:", text)
        print("\n📊 Detected Emotions:")
        for r in sorted_results:
            print(f"{r['label']}: {round(r['score'], 3)}")

        print(f"\n👉 Final Emotion: {top_emotion} (Confidence: {round(confidence, 3)})")

        return top_emotion

    except Exception as e:
        print("❌ Error occurred:", str(e))
        return None


# ---- Run Program ----
if __name__ == "__main__":
    print("🧠 Emotion Detector (type 'exit' to quit)\n")

    while True:
        user_input = input("Enter your text: ")

        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break

        if user_input.strip() == "":
            print("⚠️ Please enter some text\n")
            continue

        detect_emotion(user_input)
        print("\n" + "-"*50 + "\n")
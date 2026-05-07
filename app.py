def detect_mood(text):

    text = text.lower()

    # KEYWORD-BASED DETECTION

    sadness_words = [
        "sad", "cry", "depressed", "unhappy",
        "lonely", "heartbroken", "down",
        "upset", "not okay", "feeling low",
        "broken", "hurt", "bad"
    ]

    anger_words = [
        "angry", "mad", "furious",
        "hate", "annoyed", "rage",
        "frustrated"
    ]

    joy_words = [
        "happy", "great", "awesome",
        "excited", "amazing", "good"
    ]

    love_words = [
        "love", "romantic", "cute",
        "beautiful", "adore", "miss you"
    ]

    fear_words = [
        "fear", "afraid", "scared",
        "anxious", "worried", "nervous"
    ]

    surprise_words = [
        "wow", "surprised", "shocked",
        "unexpected", "omg"
    ]

    # CHECK KEYWORDS FIRST

    for word in sadness_words:
        if word in text:
            return "sadness"

    for word in anger_words:
        if word in text:
            return "anger"

    for word in joy_words:
        if word in text:
            return "joy"

    for word in love_words:
        if word in text:
            return "love"

    for word in fear_words:
        if word in text:
            return "fear"

    for word in surprise_words:
        if word in text:
            return "surprise"

    # FALLBACK SENTIMENT ANALYSIS

    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity

    if polarity > 0.5:
        return "joy"

    elif polarity > 0:
        return "love"

    elif polarity < -0.5:
        return "sadness"

    elif polarity < 0:
        return "anger"

    else:
        return "neutral"

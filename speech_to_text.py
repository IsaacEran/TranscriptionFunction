import requests
import azure.functions as func
from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, AudioDataStream
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Set up Speech Service config
    speech_config = SpeechConfig(subscription="8712c680f7204f789f90e6864cd385f0", region="westeurope", speech_recognition_language="he-IL")

    # Set up Text Analytics config
    ta_credential = AzureKeyCredential("8712c680f7204f789f90e6864cd385f0")
    ta_client = TextAnalyticsClient(endpoint="https://voicevectrapoc.cognitiveservices.azure.com/", credential=ta_credential)

    # Get the audio file from the request body
    audio_data = req.body.read()

    # Convert the audio data to a stream
    audio_stream = AudioDataStream(audio_data)

    # Transcribe the audio using Speech Service
    recognizer = SpeechRecognizer(speech_config=speech_config, audio=audio_stream)
    result = recognizer.recognize_once()

    # Get the transcribed text
    transcript = result.text

    # Analyze the transcript using Text Analytics
    analysis = ta_client.analyze_sentiment(transcript)

    # Create a response object
    response = func.HttpResponse(
        f"Transcript: {transcript}, Sentiment: {analysis.sentiment}",
        mimetype="text/plain"
    )

    return response
# Chatbot

## Multilingual College Enquiry Chatbot with Voice Assistant

### 🔎Brief Description:
  A smart web-based chatbot that helps students and parents with college-related queries in real-time. It supports both text and voice-based interaction (STT & TTS) using multilingual capability, offering seamless communication in English, and optionally Tamil, Hindi, and Telugu.

### ⚙️ Working Methodology:

 #### 1.User Interaction
   User types a question in the chat interface.
   
   Example: "What is the admission fee?" or in other languages like Hindi or Tamil.

 #### 2.Language Detection:
   The chatbot detects the input language using the googletrans library.

 #### 3.Intent Matching:
   It compares the user’s message with predefined patterns stored in an intents.json file using regular expressions.
   Each pattern is associated with a specific tag and corresponding response.

#### 4.Generate Response:
   Once a match is found, the corresponding answer is fetched.
   The bot translates this response into the detected input language.

#### 5.Return Response:
   The translated answer is displayed in the chat with the label "College:".Spoken aloud using the SpeechSynthesis API in JavaScript (SpeechSynthesisUttence) 

#### 6.Typing Animation & UI:
   Before the response is shown, a brief "College is typing..." animation appears to improve user experience.
   The entire UI is clean, colorful, and responsive across devices.

### 🛠️ Technologies Used:
  #### 🔧 Backend:
1.Python 3

2.Flask – for routing and server logic

3.Regex – for matching queries

4.googletrans – for automatic language detection and translation

5.intents.json – for storing question patterns and predefined responses

6.Speech Recognition - Web Speech API

7.TTS (Voice Output) - Web Speech Synthesis API

  #### 🎨 Frontend:
1.HTML – for page structure

2.CSS – for styling and elegant design

3.JavaScript – for chatbot interaction and typing animation

#### 🧪 Testing Tools:
1.Manual test cases using more than 25 sample queries

2.Multilingual test input/output validation

### Final output:

![image alt](https://github.com/user-attachments/assets/4223c34b-4b2b-492c-a129-9f5b0722d406)


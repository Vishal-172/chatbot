# Chatbot

## Multilingual College Enquiry Chatbot using Flask

### 🔎Brief Description:
  The Multilingual College Enquiry Chatbot is a rule-based web chatbot application designed to answer frequently asked questions (FAQs) about a college. It supports multiple languages using Google Translate API, ensuring accessibility for users from various linguistic backgrounds. The chatbot is built with Flask as the backend framework and a responsive, elegant frontend using HTML/CSS/JavaScript.Users can ask questions like college timings, hostel fees, available courses, eligibility, and more. The chatbot detects the user's language, processes the query, matches it with predefined patterns, and responds accurately in the same language.

### ⚙️ Working Methodology:

 #### 1.User Input:
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
   The translated answer is displayed in the chat with the label "College:".

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

  #### 🎨 Frontend:
1.HTML – for page structure

2.CSS – for styling and elegant design

3.JavaScript – for chatbot interaction and typing animation

#### 🧪 Testing Tools:
1.Manual test cases using more than 25 sample queries

2.Multilingual test input/output validation

#Blue Baguette

###Our Project
Blue Baguette generates conversational lessons based off personal experiences which are tailored to each specific user. Everyone learns differently from their use of words to style of learning and Blue Baguette’s takes that into account.

###The Data
The user will be able to generate these personalized lessons from three different sources.
The choices include choosing from the users favorite book, show or their own conversations (synced from their phone). From these choices, Blue Baguette’s AI will be able to gather enough information of how the user communicates and formulate a lesson catered for them. Blue Baguette is the conversational chatbot instructor that will be able to have conversations and play games with the users. Additionally, users will have incentives to learn with the ability to add friends. Blue Baguette’s immersive teaching style is the smarter, faster and more efficient way to learn a new language.


###The Technology
Our product was written using a React.js front end and Express.js back end. Our UI was influenced by the ideas expressed in IBM’s Design Language and utilizes Carbon Components. Data was collected from Springfield! Springfield!, an online repository of thousands of TV show episode scripts, using Python modules, requests and bs4. Phrases were parsed from this data and stored in a Pandas DataFrame in Python. Each phrase was translated using Watson Translation services and each translation was analyzed using Watson’s Natural Language Understanding to determine sentiment and extract concepts. Furthermore, phrase syntax was derived by the use of the Python library, SpaCy. After analysis, data was ported to our NoSQL database, IBM Cloudant which gives JSON formatted objects to the core of our app interface, Watson Assistant. The synergy between IBM Cloudant and Watson Assistant is provided by IBM Cloud Functions and the final product was deployed to IBM Cloud using a Kubernetes Cluster.

###Our files

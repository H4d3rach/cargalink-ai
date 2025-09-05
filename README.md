# CargaLink CDMX - AI Services

AI services for **CargaLink CDMX**, a web application developed as part of a **Bachelor’s Thesis at ESCOM (IPN)**.  
This repository contains the **Artificial Intelligence components** that support the platform:  

- **Recommendation System** – Helps client companies choose the most suitable transport providers.  
- **Chatbot** – Provides FAQ assistance and guides users through the platform.  

You can find the backend repository [here](https://github.com/Shutman-ZTAY/CargaLink-BackEnd/)
You can find the frontend repository [here](https://github.com/H4d3rach/CargaLink-Frontend/)

![Chatbot view](chatbot.jpg)

---

## Project Overview

CargaLink CDMX connects small and medium-sized freight transport companies with businesses that require cargo services.  
The AI layer enhances the user experience by:  

1. **Recommendation System**  
   - Uses **cosine similarity** and **preference vectors** to suggest the best transport companies.  
   - Takes into account client preferences such as price, reliability, quality of service.  
   - Continuously improves as users provide feedback and ratings.  

2. **Chatbot (NLP-based)**  
   - Provides answers to frequently asked questions.  
   - Assists users with basic navigation and platform usage.  
   - Reduces resistance to adopting new technology by offering immediate help.  

---

## Features

- **Recommendation Engine**  
  - Computes similarity between client preferences and transport companies.  
  - Returns ranked recommendations to the backend API.  

- **Chatbot**  
  - Answers predefined FAQ queries.  
  - Built with Natural Language Processing (NLP).  
  - Easily extensible to support more queries and conversational flows.  

- **Backend Integration**  
  - Provides recommendations and chatbot responses via REST APIs.  

---

## Tech Stack

- **Language:** Python 3  
- **Frameworks/Libraries:**  
  - Flask (REST API)  
  - scikit-learn (cosine similarity, vector operations)  

---

## Contact
- Developed as a Bachelor’s Thesis project at the Escuela Superior de Cómputo (ESCOM - IPN)
- Under the supervision of M. en C. Gabriela de Jesús López Ruíz.
- Developers:
  - [Alejandre Dominguez Alan José](https://github.com/H4d3rach)
  - [Estanislao Castro Ismael](https://github.com/Shutman-ZTAY)
  - [Gil Calderón Karla](https://github.com/karla-gilcal)

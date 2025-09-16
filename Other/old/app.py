from flask import Flask, request, jsonify, render_template_string
import json

app = Flask(__name__)

qa_data = [ 
    # ⛔ Paste your full JSON Q&A data here
    {
        "id": "Admission in collage.",
        "questions": [
            "admission in mvit clg",
            "admission in mit clg",
            "I want to put admission in mvit clg",
            "I want to put admission in mit clg",
            "I want to put admission for AIML course in your collage.",
            "I want to put admission for IOT course in your collage.",
            "I want to put admission for FT course in your collage.",
            "I want to put admission for RA course in your collage.",
            "I want to put admission for MECH course in your collage.",
            "I want to put admission for IT course in your collage.",
            "I want to put admission for CSE course in your collage.",
            "I want to put admission for ECE course in your collage.",
            "I want to put admission for EEE course in your collage.",
            "admission for EEE."
        ],
        "answer": "https://forms.gle/rCcmmLxLe1waj3tJ8 (you can put your admission by using this link)"
    },
    {
        "id": "AIML_STAFF",
        "questions": [
            "aiml mentors",
            "aiml professors",
            "aiml teachers",
            "aiml staff",
            "aiml faculty"
        ],
        "answer": "1.Mr.R. Raj Bharath https://ibb.co/HtK7Hwy          \n                                                                                                                                                    2.Mrs.K. ANUPRIYA https://www.google.com/url?q=http%3A%2F%2Faiml_staff&sa=D      \n                                                                                                                                                    3.Mrs.S.K SUGUNEDHAM https://in.docworkspace.com/d/sIA64hYOQAprqsLcG?sa=cl                                                                                                                                           \n                                                                                                                                                    4.Mrs.S. CHITRA https://in.docworkspace.com/d/sIAm4hYOQArTqsLcG?sa=cl                                           \n                                                                                                                                                    5.Mr.A. JAINULLABEEN https://in.docworkspace.com/d/sIJC4hYOQAsfqsLcG?sa=cl                         \n                                                                                                                                                    \n6.Mrs.S. LAVANYA https://in.docworkspace.com/d/sIKC4hYOQAt7qsLcG?sa=cl       \n                                                                                                                                                    7.Ms.V. NIRIMATHI https://in.docworkspace.com/d/sIPO4hYOQAvDqsLcG?sa=cl                     \n                                                                                                                                                    8.Ms.K. REVATHI https://in.docworkspace.com/d/sIFe4hYOQAoDrsLcG?sa=cl          \n                                                                                                                                                    9.Mrs.S. PRAVEENA https://in.docworkspace.com/d/sIBm4hYOQAqrrsLcG?sa=cl       \n                                                                                                                                                  10.Mrs.P. SUGANYA https://in.docworkspace.com/d/sIFS4hYOQArnrsLcG?sa=cl                                          \n                                                                                                                                                  11.Mr.R. RENGA NAYAGI https://in.docworkspace.com/d/sIIW4hYOQAtXrsLcG?sa=cl                                                                                                                                             \n                                                                                                                                                        They are the faculty of AIML in 2024-25. You can also check the faculty details by clicking the link next to their name."
    },
    {
        "id": "Bot name.",
        "questions": [
            "your name.",
            "what is your name.",
            "tell me your name."
        ],
        "answer": "My name is AK."
    },
    {
        "id": "bus_clg",
        "questions": [
            "mvit fan",
            "buses in mvit clg",
            "buses in mvit",
            "mvit bus routes",
            "mvit bus stops",
            "manakula vinayagar institute of technology buses",
            "mvit bus details",
            "clg bus details",
            "clg bus"
        ],
        "answer": "You can also track the location of the bus by using ( Ride map ) app which is available in play store. [but the student who not using the clg bus can't able to track it]"
    },
    {
        "id": "canteen",
        "questions": [
            "canteen food",
            "foods available in manakula vinayagar institute of technology",
            "food in collage canteen",
            "what are the food available in canteen",
            "ground floor canteen menu",
            "canteen menu"
        ],
        "answer": "The clg canteen menu is given below"
    },
    {
        "id": "clg_estabilsed",
        "questions": [
            "clg started details",
            "clg opening details",
            "when did the collage established"
        ],
        "answer": "manakula vinayager institute of technology was started at 2008 in madagadipet. and it was approved by AICTE. and also this institute was accredited by NAAC with 'A; grade and NBA."
    },
    {
        "id": "clg_information",
        "questions": [
            "mvit web page",
            "clg website",
            "clg web link",
            "mvit website",
            "mvit clg",
            "mit collage",
            "your clg website",
            "your clg web",
            "your collage website",
            "I want details about your collage",
            "I want details about my collage",
            "give some information about my collage",
            "give some information about your collage"
        ],
        "answer": "https://mvit.edu.in/                                                                                                              (you can visit our clg website)"
    },
    {
        "id": "clg_location",
        "questions": [
            "give me the information were the clg is located",
            "mvit location",
            "mvit in map",
            "clg location in map",
            "clg location in google map",
            "clg map",
            "where did the collage located",
            "collage location link",
            "collage location"
        ],
        "answer": "Manakula vinayagar institute of technology was located in Madagadipet. ( you can also use the given link to find the exact location of our collage) https://maps.app.goo.gl/Z15uPr65jNhRfe117"
    },
    {
        "id": "computer_lab",
        "questions": [
            "cse lab",
            "manakula vinayagar institute of technology computer lab",
            "cs lab in mvit clg",
            "computer lab in mvit",
            "photo of computer lab",
            "images of cse lab"
        ],
        "answer": "Answer not available"
    },
    {
        "id": "courses in our clg",
        "questions": [
            "course in our clg",
            "what are the engineering courses offered in your collage.",
            "courses in mvit collage.",
            "courses in your clg.",
            "courses in your collage.",
            "what  are courses in your clg.",
            "what  are courses in your collage."
        ],
        "answer": "I have only information about engineering branch. so the engineering courses offered by our collage in the year of 2024-25 are:                                                                                                 EEE.                                                                                                                                                                       ECE.                                                                                                                                                                           CSE.                                                                                                                                                                           IT.                                                                                                                                                               MECH.                                                                                                                                                     RA.                                                                                                                                                            FT.                                                                                                                                                         IOT.                                                                                                                                                                   AIML."
    },
    {
        "id": "Default Welcome Intent",
        "questions": [
            "just going to say hi",
            "heya",
            "hello hi",
            "hai",
            "hey there",
            "hi there",
            "greetings",
            "hey",
            "long time no see",
            "hello",
            "lovely day isn't it",
            "I greet you",
            "hello again",
            "hi",
            "hello there",
            "a good day"
        ],
        "answer": "Hello! How can I help you?"
    },
    {
        "id": "digital_library",
        "questions": [
            "internet library",
            "online library",
            "other library",
            "digital library in manakula vinayagar institute of technology , pondicheery",
            "digital library in mvit pondicheery",
            "digital library"
        ],
        "answer": "Our Digital Library facilitates students and faculty members a modern digital learning approach with technically sophisticated environment to enhance their knowledge through e-journals &  e \u2013 books with unlimited access"
    },
    {
        "id": "eee_staff",
        "questions": [
            "aiml mentors",
            "EEE teachers",
            "eee professers",
            "eee staff",
            "eee faculty"
        ],
        "answer": "1.Dr.C. SHANMUGASUNDARAM https://in.docworkspace.com/d/sII24hYOQAsy3sLcG?sa=cl                                           \n                                                                                                                  2.Dr.K. SEDHURAMAN https://in.docworkspace.com/d/sIAK4hYOQAva3sLcG?sa=cl                                                                                                                                           \n                                                                                                                                                    3.Mr.S. RAJKUMAR https://in.docworkspace.com/d/sIOa4hYOQAo24sLcG?sa=cl         \n                                                                                                                                                     \n4.Mr.N. AMARABALAN https://in.docworkspace.com/d/sIFG4hYOQAru4sLcG?sa=cl    \n                                                                                                                                                    \n5.Mr.D. BALAJI https://in.docworkspace.com/d/sICO4hYOQAq_SsLcG?sa=cl             \n                                                                                                                                                    \n6.Mr. DMURUGANANDHAN https://in.docworkspace.com/d/sIMW4hYOQAr_SsLcG?sa=cl         \n                                                                                                                                                    7.Mrs.R. UMAMAHESWARI https://in.docworkspace.com/d/sIJW4hYOQAtDSsLcG?sa=cl                                                                                                                                           \n                                                                                                                                                   8.Mrs.S. SANTHALAKSHMY https://in.docworkspace.com/d/sIGW4hYOQAuDSsLcG?sa=cl                                     \n                                                                                                                                                   9.Mrs.R. MUTHUNAGAI https://in.docworkspace.com/d/sIF-4hYOQAvLSsLcG?sa=cl    \n                                                                                                                                                 10.Mrs.R. PRIYA https://in.docworkspace.com/d/sIAK4hYOQAoLTsLcG?sa=cl         \n                                                                                                                                                  11.Mrs.J. VIJAYA RAGHAVAN https://in.docworkspace.com/d/sIO-4hYOQApHTsLcG?sa=cl                                                                                                       \n                                                                                                                                                  12.Mr.S. VEERAMANIKANDAN https://in.docworkspace.com/d/sINS4hYOQArvTsLcG?sa=cl                                      \n                                                                                                                                                  13.Mr.P. TAMIZHARASAN https://in.docworkspace.com/d/sIH64hYOQAtDTsLcG?sa=cl                                                                                                                                    \n                                                                                                                                                  14.Mrs. SUVEDHA https://in.docworkspace.com/d/sIOq4hYOQAt7TsLcG?sa=cl         \n                                                                                                                                                        They are the faculty of EEE in 2024-25. You can also check the faculty details by clicking the link next to their name."
    },
    {
        "id": "1st year fees for aiml",
        "questions": [
            "artificial intelligence and machine learning fees for 1st year",
            "first year aiml fees",
            "1st fees for AIML.",
            "fees for AIML"
            "tell me the fees structure for AIML in first year"
        ],
        "answer": "The fees structure for AIML in 1st yeart in 2025-26.for centac students is Rs:52,700 and for  management is Rs:81,500."
    },
    {
        "id": "1st year fees for CSC.",
        "questions": [
            "1st year computer science and engineering fees",
            "computer science fees for first year",
            "cse fees fro 1st year",
            "fees for CSE.",
            "tell me the fees structure for CSE dept in 1st year"
        ],
        "answer": "The fees structure for CSE in 1st year in 2025-26.for centac students is Rs:62,700 and for management students is Rs:91,500"
    },
    {
        "id": "1st year fees for ECE",
        "questions": [
            "electronics and communication engineering fees for 1st year",
            "1st year ece fees",
            "fess details for ECE in mvit",
            "tell me the first year fees structure for ECE."
        ],
        "answer": "The fess structure for ECE in 1st year in 2025-26.for centac students is Rs:62,700 and for management students is Rs:81,500."
    },
    {
        "id": "1st year fees for FT",
        "questions": [
            "food technology fees",
            "ft fees",
            "fees for FT.",
            "tell me the fees structure for FT."
        ],
        "answer": "The fees structure for FT in 2025-26.for centac students is Rs:52,700 and for management students is Rs:71,500."
    },
    {
        "id": "fees for IOT",
        "questions": [
            "information of things fees",
            "iot fees",
            "fees for IOT.",
            "tell me the fees structure for IOT."
        ],
        "answer": "The fees structure IOT  for in 2024-25.for centac students is Rs:52,700 and for management students is Rs:81,500."
    },
    {
        "id": "fees for IT",
        "questions": [
            "information technology fees",
            "it fees",
            "fees for IT.",
            "tell me the fees structure for IT."
        ],
        "answer": "The fees structure for IT in 2024-25.for centac students is Rs:62,700 and for management students is Rs:91,500."
    },
    {
        "id": "fees for MECH",
        "questions": [
            "mechanical engineering fees",
            "mech fees",
            "fees for MECH.",
            "tell me the fees structure for \n MECH."
        ],
        "answer": "The fees structure for MECH in 2024-25.for management students is Rs:52,700 and for centac students is Rs:52,700."
    },
    {
        "id": "fees for RA",
        "questions": [
            "robotics and automation fees",
            "robotics fees",
            "fees for robotics",
            "fees for RA",
            "tell me the fees structure for \n RA."
        ],
        "answer": "The fees structure for RA in 2024-25.for centac students is Rs:52,700 and for management students is Rs:71,500."
    },
    {
        "id": "fess for EEE",
        "questions": [
            "electrical and electronic engineering fees",
            "eee fees",
            "fees for EEE.",
            "fees structure for EEE.",
            "tell me the fees structure for EEE."
        ],
        "answer": "The fess structure for EEE in 2024-25.for management students is Rs:52,700 and for centac students is Rs:52,700."
    },
    {
        "id": "FT_STAFF",
        "questions": [
            "ft professors",
            "ft techers",
            "ft mentors",
            "ft faculty",
            "ft staff"
        ],
        "answer": "1.Dr.D. Tiroutchelvame https://in.docworkspace.com/d/sICO4hYOQAsf5sLcG?sa=cl  \n                                                                                                                                                    2.Dr.S. Aruna https://in.docworkspace.com/d/sIEy4hYOQAvv5sLcG?sa=cl                  \n                                                                                                                                                    3.Dr.S. Santhalakshmy https://in.docworkspace.com/d/sICe4hYOQAor6sLcG?sa=cl   \n                                                                                                                                                    4.Dr.R. Baghya Nisha https://in.docworkspace.com/d/sILm4hYOQApj6sLcG?sa=cl                                        \n                                                                                                                                                    5.Er.R. Shailajha https://in.docworkspace.com/d/sIGi4hYOQAqn6sLcG?sa=cl            \n                                                                                                                                                    6.Er. Vimal,H https://in.docworkspace.com/d/sIKK4hYOQArr6sLcG?sa=cl                   \n                                                                                                                                                    7.Er.S. Indumathi https://in.docworkspace.com/d/sIG64hYOQAsb6sLcG?sa=cl                   \n                                                                                                                                                    8.Er.M .Nithyapriya (link is not available)                                                                              \n                                                                                                                                                     They are the faculty of FT in 2024-25. You can also check the faculty details by clicking the link next to their name."
    },
    {
        "id": "good afternoon",
        "questions": [
            "happy afternoon.",
            "good afternoon.",
            "hi, good afternoon."
        ],
        "answer": "hello, good afternoon."
    },
    {
        "id": "good night",
        "questions": [
            "have a good night.",
            "good night",
            "hi, good night."
        ],
        "answer": "hello, good night."
    },
    {
        "id": "happy morning.",
        "questions": [
            "happy morning.",
            "good morning.",
            "hi good morning."
        ],
        "answer": "good morning, how can I help you."
    },
    {
        "id": "image_of_clg",
        "questions": [
            "manakula vinayagar institute of technology images",
            "mvit photos",
            "mvit images"
        ],
        "answer": "Answer not available"
    },
    {
        "id": "iot_staff",
        "questions": [
            "information of things faculty",
            "iot teachers",
            "iot mentors",
            "iot facultys",
            "iot professors",
            "iot staffs"
        ],
        "answer": "1.Dr.N. PALANIVEL ( Link is not available )     \n                                                                                                                                                    2.Mrs.V.SUGANYA ( Link is not available )                                                                                                                                            \n                                                                                                                                                      3.Mr.V.KUMARAGURU https://in.docworkspace.com/d/sIPC4hYOQArX1urcG?sa=cl         \n                                                                                                                                                    4.Mrs.K.C NITHYASREE https://in.docworkspace.com/d/sIFe4hYOQAv71urcG?sa=cl                    \n                                                                                                                                                    5.Mr.G.KEERTHIRAAJ ( Link is not available )                                                                                                           \n                                                                                                                                                    6.Ms.S.ADOLPHINE SHYNI https://in.docworkspace.com/d/sICu4hYOQAov2urcG?sa=cl                                                                                                                                           \n                                                                                                                                                    7.Mrs.K.KAVITHA https://in.docworkspace.com/d/sIAG4hYOQApj2urcG?sa=cl         \n                                                                                                                                                    \n 8.Ms.A.SHEERIN https://in.docworkspace.com/d/sIKC4hYOQAqT2urcG?sa=cl            \n                                                                                                                                                    9.Mr.U.MURUGANANTHAM ( Link is not available )                                                                                    \n                                                                                                                                                    They are the faculty of IOT in 2024-25. You can also check the faculty details by clicking the link next to their name."
    },
    {
        "id": "Library",
        "questions": [
            "library in manakula vinayagar institute of technology",
            "mvit library images",
            "library images",
            "library in our clg",
            "library"
        ],
        "answer": "The College Central library has a collection of 17415 books, in different subjects like, Basic Sciences, Engineering & Technology and Management etc., Open access system is followed in the library. All the library transactions are computerized & Bar coded."
    },
    {
        "id": "mech_staff",
        "questions": [
            "mech staff",
            "mech teacher",
            "mech faculty",
            "mech professors",
            "mechanical engineering faculty"
        ],
        "answer": "1.Dr.B.RADJARAM https://in.docworkspace.com/d/sIMm4hYOQAr6Eu7cG?sa=cl                                                \n                                                                                                                                                    2.Mr.K.KARTHIGAYAN https://in.docworkspace.com/d/sINO4hYOQAtSEu7cG?sa=cl                                                                                                                                           \n                                                                                                                                                    3.Mr.K.SELVAM https://in.docworkspace.com/d/sIKS4hYOQAuaEu7cG?sa=cl                                       \n                                                                                                                                                    4.Mr.B.VASANTH https://in.docworkspace.com/d/sIHC4hYOQAviEu7cG?sa=cl                                                        \n                                                                                                                                                    5.Mr.S.GANESHKUMAR https://in.docworkspace.com/d/sIHC4hYOQAo6Fu7cG?sa=cl                                                                                                                                                               \n                                                                                                                                                    6.Mr.A.THIAGARAJAN https://in.docworkspace.com/d/sIEq4hYOQApyFu7cG?sa=cl                      \n                                                                                                                                                    7.Mr.KARTHIKEYAN https://in.docworkspace.com/d/sIDy4hYOQArOFu7cG?sa=cl                         \n                                                                                                                                                    8.Mr.J.SUGUMARAN https://in.docworkspace.com/d/sICW4hYOQAseFu7cG?sa=cl                          \n                                                                                                                                                    9.Mr.R.RANJIT KUMAR https://in.docworkspace.com/d/sIM-4hYOQAtiFu7cG?sa=cl          \n                                                                                                                                                  10.Ms.S.SUGUNYA https://in.docworkspace.com/d/sIHK4hYOQAu-Fu7cG?sa=cl                   \n11.Mr.R.ILANDJEZIANR https://in.docworkspace.com/d/sIOy4hYOQAoKGu7cG?sa=cl                                                                                                                                  12.Dr.A.MATHIARASU https://in.docworkspace.com/d/sIGS4hYOQApmGu7cG?sa=cl                                                                                                                                    13.Dr.P.NATARAJAN https://in.docworkspace.com/d/sID-4hYOQAraGu7cG?sa=cl              \n14.Mr.S.KRISHNA KUMAR https://in.docworkspace.com/d/sIHq4hYOQAtSGu7cG?sa=cl                                                                                                                                        15.Mrs.G.DEEBA https://in.docworkspace.com/d/sIAu4hYOQAvGGu7cG?sa=cl                       16.Mrs.S.SHEENA https://in.docworkspace.com/d/sIK24hYOQApaHu7cG?sa=cl              \nThey are the faculty of MECH in 2024-25. You can also check the faculty details by clicking the link next to their name."
    },
    {
        "id": "placement",
        "questions": [
            "placements in mvit",
            "placement in our clg",
            "student selected in company",
            "student got placement",
            "students placement record",
            "students placement",
            "placement",
            "placement records",
            "placement details"
        ],
        "answer": "Answer not available"
    },
    {
        "id": "queries_form",
        "questions": [
            "queries submission link",
            "queries link",
            "queries submission",
            "I have some queries",
            "queries form",
            "queries section",
            "where did i submit my queries"
        ],
        "answer": "You can submit your queries by using the link https://docs.google.com/forms/d/e/1FAIpQLSe5kYktZG884dUGs7As2CxX240i5yq9O4pBoL4n6sJYITlRTA/viewform?usp=sf_link"
    },
    {
        "id": "robotics_staff",
        "questions": [
            "ra staff",
            "robotics staff",
            "robotics and automation mentor",
            "robotics and automation teachers",
            "robotics and automation professors",
            "robotics and automation faculty",
            "robotics and automation staff"
        ],
        "answer": "1.Dr.V.GOVINDHAN https://in.docworkspace.com/d/sIDe4hYOQAs2JsbcG?sa=cl     \n                                                                                                                                                    2.Mr.A.BASKARAN https://in.docworkspace.com/d/sID-4hYOQApiKsbcG?sa=cl          \n                                                                                                                                                    3.Mrs.KIRUBA SANDOU https://in.docworkspace.com/d/sING4hYOQAquKsbcG?sa=cl                                                                                                                                                               \n                                                                                                                                                    4.Ms.D.JASMINE SUSILA https://in.docworkspace.com/d/sIDq4hYOQAuqKsbcG?sa=cl                                                                                                                                                \n                                                                                                                                                    5.Mrs.J.V. PESHA https://in.docworkspace.com/d/sIJu4hYOQAvmKsbcG?sa=cl                        \n                                                                                                                                                    6.Mrs.D.DHARANI https://in.docworkspace.com/d/sIPm4hYOQAoOLsbcG?sa=cl         \n                                                                                                                                                    7.Mrs.T.SUDHA ( link is not  available )                                                                                 \n                                                                                                                                                     They are the faculty of robotics and automation in 2024-25. You can also check the faculty details by clicking the link next to their name."
    },
    {
        "id": "room_num",
        "questions": [
            "class rooms allotment in manakula vinayagar institute of technology",
            "number of classes",
            "classes",
            "class room details",
            "room numbers",
            "class room allotment",
            "class rooms in mvit clg"
        ],
        "answer": "Answer not available"
    },
    {
        "id": "seats_for_cse",
        "questions": [
            "seat for computer science engineering",
            "seat for cse",
            "seat for cse in mit",
            "no of seats in cse",
            "how many seats are there for cse",
            "how many seat alloted for cse",
            "cse seats"
        ],
        "answer": "no of seats for computer science engineering in B.TECH in 2024 is... [240] and in M.TECH is ...[12]"
    },
    {
        "id": "seats_for_ece",
        "questions": [
            "seats for electronics communication engineering",
            "seat for ece",
            "seat for ece in mit",
            "no of seats in ece",
            "how many seats are there for ece",
            "how many seat alloted for ece",
            "ece seats"
        ],
        "answer": "no of seats for electronics and communication engineering  in B.TECH in 2024 is... [180] and in M.TECH is...[12]"
    },
    {
        "id": "seats_for_FT",
        "questions": [
            "seat for food technology",
            "seat for ft",
            "seat for ft in mit",
            "no of seats in ft",
            "how many seats are there for ft",
            "how many seat alloted for ft"
        ],
        "answer": "no of seats for food technology  in 2024 is... [60]"
    },
    {
        "id": "seats_for_Iot",
        "questions": [
            "seats in information of things",
            "seat for iot",
            "seat for iot in mit",
            "no of seats in iot",
            "how many seats are there for iot",
            "how many seat alloted for iot"
        ],
        "answer": "no of seats for information of things in 2024 is... [60]"
    },
    {
        "id": "seats_for_MECH",
        "questions": [
            "seat in mechanical engineering",
            "seats in mechanical",
            "seat for mech",
            "seat for mech in mit",
            "no of seats in mech",
            "how many seats are there for mech",
            "how many seat alloted for mech",
            "mech seats"
        ],
        "answer": "no of seats for mechanical engineering in 2024 is... [60]"
    },
    {
        "id": "seats_for_robotics",
        "questions": [
            "seat for robotics",
            "seat for RA in mit",
            "no of seats in robotics",
            "how many seats are there for RA",
            "how many seat alloted for RA"
        ],
        "answer": "no of seats for robotics in 2024 is... [60]"
    },
    {
        "id": "seat_for_aiml",
        "questions": [
            "seats for artificial engineering and machine learning",
            "aiml seats",
            "how many seat alloted for aiml",
            "how many seats are there for aiml",
            "no of seats in aiml",
            "seat for aiml in mit",
            "seat for aiml"
        ],
        "answer": "no of seats for artificial and machine learning in 2024 is... [180]"
    },
    {
        "id": "seat_for_eee",
        "questions": [
            "electrical and electronics engineering",
            "eee seat in 2024",
            "seat for eee",
            "seat for eee in mit",
            "no of seats in eee",
            "how many seats are there for eee",
            "how many seat alloted for eee",
            "eee seats"
        ],
        "answer": "no of seats for electrical and electronics engineering in 2024 is... [60]"
    },
    {
        "id": "seat_for_IT",
        "questions": [
            "seats for information technology",
            "seat for it",
            "seat for it in mit",
            "no of seats in it",
            "how many seats are there for it",
            "how many seat alloted for it",
            "it seats"
        ],
        "answer": "no of seats for information technology in 2024 is... [120]"
    },
    {
        "id": "sports",
        "questions": [
            "sports activity",
            "sports award",
            "extra cricular activity eca",
            "sports in mvit",
            "sports",
            "sports in your clg",
            "what are the sports in our clg"
        ],
        "answer": "silver medal in 100m swimming competition"
    },
    {
        "id": "syllabus_aiml_sem1",
        "questions": [
            "aiml syllabus for semester1",
            "sem1 aiml syllabus",
            "sem1 syllabus for aiml",
            "aiml sem1 syllabus",
            "phy syllabus for aiml",
            "m1 syllabus for aiml",
            "bee syllabus for aiml",
            "semester 1 syllabus for aiml",
            "syllabus for aiml sem 1",
            "syllabus for aiml",
            "aiml syllabus"
        ],
        "answer": "sem1 syllabus for aiml is given below"
    },
    {
        "id": "syllabus_aiml_sem2",
        "questions": [
            "aiml syllabus for semester2",
            "aiml syllabus for 2semester",
            "aiml syllabus 2sem",
            "sem2 syllabus for aiml",
            "aiml sem2 syllabus"
        ],
        "answer": "Problem solving and programming"
    },
    {
        "id": "syllabus_aiml_sem3",
        "questions": [
            "sem3 aiml",
            "aiml sem3",
            "syllabus for aiml semester3",
            "aiml semester3 syllabus",
            "sem3 syllabus aiml",
            "syllabus for sem3 aiml",
            "syllabus for aiml sem3"
        ],
        "answer": "These are the sem3 syllabus for aiml"
    },
    {
        "id": "syllabus_cse_sem1",
        "questions": [
            "cse syllabus",
            "syllabus for computer science engineering",
            "semester1 cse syllabus",
            "cse syllabus for sem1"
        ],
        "answer": "BEE syllabus"
    },
    {
        "id": "vision_mission",
        "questions": [
            "clg mission",
            "clg vision",
            "vision and mission",
            "clg vision and mission",
            "vision and mission of the manakula vinayagar institute of technology collage",
            "vision and mission of the mvit collage"
        ],
        "answer": "The vision and mission of the clg is given below"
    },
    {
        "id": "how are you",
        "questions": [
            "how are you",
            "hwo are you",
            "how aer you",
            "how are yuo"
        ],
        "answer": "I am Good"
    },
    {
        "id": "work",
        "questions": [
            "what can you do",
            "what is your work",
            "waht is work",
            "tell me about your nwork",
            "tell me about your work",
            "what are you doing"
        ],
        "answer": "I give information about MVIT clg"
    },
    {
        "id": "doing",
        "questions": [
            "how are you doing",
            "how are you"
        ],
        "answer": "I am doing Good"
    },
]

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>MVIT Chatbot</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f8f9fa; }
        #chatbox { max-width: 800px; margin: 50px auto; padding: 30px; background: #ffffff; border-radius: 12px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        .message { margin: 10px 0; }
        .user { text-align: right; color: #0d6efd; }
        .bot { text-align: left; color: #198754; }
        .bubble { padding: 10px 15px; border-radius: 15px; display: inline-block; max-width: 80%; }
        .user .bubble { background: #e7f1ff; }
        .bot .bubble { background: #e9fbe9; }
    </style>
</head>
<body>
    <div id="chatbox" class="container">
        <h3 class="text-center mb-4">🎓 MVIT Chatbot</h3>
        <div id="chatlog" class="mb-3"></div>
        <div class="input-group">
            <input type="text" id="user_input" class="form-control" placeholder="Ask something...">
            <button class="btn btn-primary" onclick="send()">Send</button>
        </div>
    </div>

    <script>
        function send() {
            let input = document.getElementById("user_input");
            let msg = input.value.trim();
            if (!msg) return;

            let chatlog = document.getElementById("chatlog");
            chatlog.innerHTML += "<div class='message user'><div class='bubble'>" + msg + "</div></div>";

            fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: msg })
            })
            .then(res => res.json())
            .then(data => {
                chatlog.innerHTML += "<div class='message bot'><div class='bubble'>" + data.reply + "</div></div>";
                input.value = "";
                chatlog.scrollTop = chatlog.scrollHeight;
            });
        }

        document.getElementById("user_input").addEventListener("keypress", function(e) {
            if (e.key === "Enter") send();
        });
    </script>
</body>
</html>
'''

def find_answer(user_input):
    user_input = user_input.lower()
    for item in qa_data:
        for q in item["questions"]:
            if user_input in q.lower():
                return item["answer"]
    return "Sorry, I don't have an answer for that."

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get("message", "")
    reply = find_answer(message)
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
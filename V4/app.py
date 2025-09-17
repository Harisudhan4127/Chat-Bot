from flask import Flask, request, jsonify, render_template
import difflib
from spellchecker import SpellChecker

app = Flask(__name__)

# -------------------- Q&A DATA --------------------

qa_data = [
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
            "admission for EEE.",
            "admission"
        ],
        "answer": "https://forms.gle/rCcmmLxLe1waj3tJ8 <br> (you can put your admission by using this link)"
    },
    {
        "id": "AIML_STAFF",
        "questions": [
            "aiml mentors",
            "aiml professors",
            "aiml teachers",
            "aiml staff",
            "aiml faculty",
            "staff aiml"
        ],
        "answer": "1.Mr.R. RAJ BHARATH <br> img:/static/images/computer_lab.jpeg <br>"
        "2.Mrs.S.K SUGUNEDHAM <br> img:/static/images/sugunedham_aiml.jpeg <br>"
        "3.Mrs.S. CHITRA <br> https://in.docworkspace.com/d/sIAm4hYOQArTqsLcG?sa=cl <br>"
        "4.Mr.A. JAINULLABEEN <br> https://in.docworkspace.com/d/sIJC4hYOQAsfqsLcG?sa=cl <br>"
        "5.Mrs.S. LAVANYA <br> https://in.docworkspace.com/d/sIKC4hYOQAt7qsLcG?sa=cl  <br>"
        "6.Ms.V. NIRIMATHI <br> https://in.docworkspace.com/d/sIPO4hYOQAvDqsLcG?sa=cl  <br>"
        "7.Ms.K. REVATHI <br> https://in.docworkspace.com/d/sIFe4hYOQAoDrsLcG?sa=cl   <br>"
        "8.Mrs.S. PRAVEENA <br> https://in.docworkspace.com/d/sIBm4hYOQAqrrsLcG?sa=cl  <br>"
        "9.Mrs.P. SUGANYA <br> https://in.docworkspace.com/d/sIFS4hYOQArnrsLcG?sa=cl  <br>"
        "10.Mr.R. RENGA NAYAGI <br> https://in.docworkspace.com/d/sIIW4hYOQAtXrsLcG?sa=cl  <br>"
        "They are the faculty of AIML in 2025-26. You can also check the faculty details by clicking the link next to their name."
    },
    {
        "id": "Bot name.",
        "questions": [
            "your name.",
            "what is your name.",
            "tell me your name.",
            "name"
        ],
        "answer": "My name is AK."
    },
    {
        "id": "bus_clg",
        "questions": [
            "mvit bus",
            "buses in mvit clg",
            "buses in mvit",
            "mvit bus routes",
            "mvit bus stops",
            "manakula vinayagar institute of technology buses",
            "mvit bus details",
            "clg bus details",
            "clg bus",
            "bus details"
        ],
        "answer": "img:/static/images/bus_fees.jpeg"
    },
    {
        "id": "bus image",
        "questions": [
            "mvit bus image",
            "buses images mvit clg",
            "buses pic in mvit",
            "mvit bus pics",
            "mvit bus pictures",
            "manakula vinayagar institute of technology bus image",
            "mvit bus pic",
            "clg bus photo",
            "clg photos"
        ],
        "answer": "img:/static/images/bus.jpeg"
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
            "give some information about your collage",
            "web"
        ],
        "answer": "https://mvit.edu.in/<br> (you can visit our clg website)"
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
        "answer": "Manakula vinayagar institute of technology was located in Madagadipet.<br>"
        " ( you can also use the given link to find the exact location of our collage) <br>"
        "https://maps.app.goo.gl/Z15uPr65jNhRfe117"
    },
    {
        "id": "computer_lab",
        "questions": [
            "cse lab",
            "manakula vinayagar institute of technology computer lab",
            "cs lab in mvit clg",
            "computer lab in mvit",
            "photo of computer lab",
            "images of cse lab",
            "copmuter lab"
        ],
        "answer": "img:/static/images/computer_lab.jpeg"
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
        "answer": "I have only information about engineering branch.<br>"
        " so the engineering courses offered by our collage in the year of 2025-26 are:<br>"
        "EEE,<br> ECE,<br> CSE,<br> IT,<br> MECH,<br> RA,<br> FT,<br> IOT,<br> AIML,<br>"
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
        "answer": "img:/static/images/digital_library.jpeg"
    },
    {
        "id": "eee_staff",
        "questions": [
            "Eee mentors",
            "EEE teachers",
            "eee professers",
            "eee staff",
            "eee faculty",
            "staff eee"
        ],
        "answer": "1.Dr.C. SHANMUGASUNDARAM <br> https://in.docworkspace.com/d/sII24hYOQAsy3sLcG?sa=cl <br>"
        "2.Dr.K. SEDHURAMAN <br> https://in.docworkspace.com/d/sIAK4hYOQAva3sLcG?sa=cl <br>"
        "3.Mr.S. RAJKUMAR <br> https://in.docworkspace.com/d/sIOa4hYOQAo24sLcG?sa=cl <br>"
        "4.Mr.N. AMARABALAN <br> https://in.docworkspace.com/d/sIFG4hYOQAru4sLcG?sa=cl <br>"
        "5.Mr.D. BALAJI <br  https://in.docworkspace.com/d/sIMW4hYOQAr_SsLcG?sa=cl <br>"
        "7.Mrs.R. UMAMAHESWARI <br> https://in.docworkspace.com/d/sIJW4hYOQAtDSsLcG?sa=cl <br>"
        "8.Mrs.S. SANTHALAKSHMY <br> https://in.docworkspace.com/d/sIGW4hYOQAuDSsLcG?sa=cl <br>"
        "9.Mrs.R. MUTHUNAGAI <br> https://in.docworkspace.com/d/sIF-4hYOQAvLSsLcG?sa=cl  <br>"
        "10.Mrs.R. PRIYA <br> https://in.docworkspace.com/d/sIAK4hYOQAoLTsLcG?sa=cl  <br>"
        "11.Mrs.J. VIJAYA RAGHAVAN <br> https://in.docworkspace.com/d/sIO-4hYOQApHTsLcG?sa=cl <br>"
        "12.Mr.S. VEERAMANIKANDAN <br> https://in.docworkspace.com/d/sINS4hYOQArvTsLcG?sa=cl <br>"
        "13.Mr.P. TAMIZHARASAN <br> https://in.docworkspace.com/d/sIH64hYOQAtDTsLcG?sa=cl  <br>"
        "14.Mrs. SUVEDHA <br> https://in.docworkspace.com/d/sIOq4hYOQAt7TsLcG?sa=cl <br>"
        "They are the faculty of EEE in 2025-26. You can also check the faculty details by clicking the link next to their name."
    },
    {
        "id": "fees for AIML",
        "questions": [
            "artificial intelligence and machine learning fees",
            "aiml fees",
            "fees for AIML.",
            "tell me the fees structure for AIML."
        ],
        "answer": "The fees structure for AIML  in 2025-26.for centac students is Rs:52,700 and for  management is Rs:81,500."
    },
    {
        "id": "fees for CSC.",
        "questions": [
            "computer science and engineering fees",
            "computer science fees",
            "cse fees",
            "fees for CSE.",
            "tell me the fees structure for CSE."
        ],
        "answer": "The fees structure for CSE in 2025-26.for centac students is Rs:62,700 and for management students is Rs:91,500"
    },
    {
        "id": "fees for ECE",
        "questions": [
            "electronics and communication engineering fees",
            "ece fees",
            "fess for ECE",
            "tell me the fees structure for ECE."
        ],
        "answer": "The fess structure for ECE in 2025-26.for centac students is Rs:62,700 and for management students is Rs:81,500."
    },
    {
        "id": "fees for FT",
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
        "answer": "The fees structure IOT  for in 2025-26.for centac students is Rs:52,700 and for management students is Rs:81,500."
    },
    {
        "id": "fees for IT",
        "questions": [
            "information technology fees",
            "it fees",
            "fees for IT.",
            "tell me the fees structure for IT."
        ],
        "answer": "The fees structure for IT in 2025-26.for centac students is Rs:62,700 and for management students is Rs:91,500."
    },
    {
        "id": "fees for MECH",
        "questions": [
            "mechanical engineering fees",
            "mech fees",
            "fees for MECH.",
            "tell me the fees structure for MECH."
        ],
        "answer": "The fees structure for MECH in 2025-26.for management students is Rs:52,700 and for centac students is Rs:52,700."
    },
    {
        "id": "fees for RA",
        "questions": [
            "robotics and automation fees",
            "robotics fees",
            "fees for robotics",
            "fees for RA",
            "tell me the fees structure for RA."
        ],
        "answer": "The fees structure for RA in 2025-26.for centac students is Rs:52,700 and for management students is Rs:71,500."
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
        "answer": "The fess structure for EEE in 2025-26.for management students is Rs:52,700 and for centac students is Rs:52,700."
    },
    {
        "id": "FT_STAFF",
        "questions": [
            "FT professors",
            "ft techers",
            "ft mentors",
            "ft faculty",
            "f t staff"
        ],
        "answer": "1.Dr.D. Tiroutchelvame https://in.docworkspace.com/d/sICO4hYOQAsf5sLcG?sa=cl  <br>"
        "2.Dr.S. Aruna https://in.docworkspace.com/d/sIEy4hYOQAvv5sLcG?sa=cl  <br>"
        "3.Dr.S. Santhalakshmy https://in.docworkspace.com/d/sICe4hYOQAor6sLcG?sa=cl  <br>"
        "4.Dr.R. Baghya Nisha https://in.docworkspace.com/d/sILm4hYOQApj6sLcG?sa=cl  <br>"
        "5.Er.R. Shailajha https://in.docworkspace.com/d/sIGi4hYOQAqn6sLcG?sa=cl  <br>"
        "6.Er. Vimal,H https://in.docworkspace.com/d/sIKK4hYOQArr6sLcG?sa=cl  <br>"
        "7.Er.S. Indumathi https://in.docworkspace.com/d/sIG64hYOQAsb6sLcG?sa=cl  <br>"
        "8.Er.M .Nithyapriya (link is not available) <br>"
        "They are the faculty of FT in 2025-26. You can also check the faculty details by clicking the link next to their name."
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
            "IOT teachers",
            "iot mentors",
            "iot facultys",
            "iot professors",
            "iot staffs"
        ],
        "answer": "1.Dr.N. PALANIVEL <br> ( Link is not available ) <br>"
        "  2.Mrs.V.SUGANYA <br> ( Link is not available ) <br>"
        "  3.Mr.V.KUMARAGURU <br>https://in.docworkspace.com/d/sIPC4hYOQArX1urcG?sa=cl  <br>"
        "   4.Mrs.K.C NITHYASREE <br> https://in.docworkspace.com/d/sIFe4hYOQAv71urcG?sa=cl  <br>"
        "  5.Mr.G.KEERTHIRAAJ <br> ( Link is not available )  <br>"
        " 6.Ms.S.ADOLPHINE SHYNI <br> https://in.docworkspace.com/d/sICu4hYOQAov2urcG?sa=cl   <br>"
        "  7.Mrs.K.KAVITHA <br> https://in.docworkspace.com/d/sIAG4hYOQApj2urcG?sa=cl  <br>"
        " 8.Ms.A.SHEERIN <br> https://in.docworkspace.com/d/sIKC4hYOQAqT2urcG?sa=cl   <br>"
        "  9.Mr.U.MURUGANANTHAM <br> ( Link is not available )  <br>"
        " They are the faculty of IOT in 2025-26. You can also check the faculty details by clicking the link next to their name."
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
        "answer": "img:/static/images/library.jpeg"
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
        "answer": "1.Dr.B.RADJARAM <br> https://in.docworkspace.com/d/sIMm4hYOQAr6Eu7cG?sa=cl   <br>"  
        "2.Mr.K.KARTHIGAYAN <br> https://in.docworkspace.com/d/sINO4hYOQAtSEu7cG?sa=cl <br>"
        "3.Mr.K.SELVAM <br> https://in.docworkspace.com/d/sIKS4hYOQAuaEu7cG?sa=cl <br>"
        "4.Mr.B.VASANTH <br> https://in.docworkspace.com/d/sIHC4hYOQAviEu7cG?sa=cl <br>"
        "5.Mr.S.GANESHKUMAR <br> https://in.docworkspace.com/d/sIHC4hYOQAo6Fu7cG?sa=cl <br>"
        "6.Mr.A.THIAGARAJAN <br> https://in.docworkspace.com/d/sIEq4hYOQApyFu7cG?sa=cl <br>"
        "7.Mr.KARTHIKEYAN <br> https://in.docworkspace.com/d/sIDy4hYOQArOFu7cG?sa=cl <br>"
        "8.Mr.J.SUGUMARAN <br> https://in.docworkspace.com/d/sICW4hYOQAseFu7cG?sa=cl <br>" 
        "9.Mr.R.RANJIT KUMAR <br> https://in.docworkspace.com/d/sIM-4hYOQAtiFu7cG?sa=cl <br>"         
        "10.Ms.S.SUGUNYA <br> https://in.docworkspace.com/d/sIHK4hYOQAu-Fu7cG?sa=cl <br>" 
        "11.Mr.R.ILANDJEZIANR <br> https://in.docworkspace.com/d/sIOy4hYOQAoKGu7cG?sa=cl <br>" 
        "12.Dr.A.MATHIARASU <br> https://in.docworkspace.com/d/sIGS4hYOQApmGu7cG?sa=cl  <br>"
        "13.Dr.P.NATARAJAN <br> https://in.docworkspace.com/d/sID-4hYOQAraGu7cG?sa=cl  <br>"
        "14.Mr.S.KRISHNA KUMAR <br> https://in.docworkspace.com/d/sIHq4hYOQAtSGu7cG?sa=cl <br>"
        "15.Mrs.G.DEEBA <br> https://in.docworkspace.com/d/sIAu4hYOQAvGGu7cG?sa=cl  <br>"
        "16.Mrs.S.SHEENA <br> https://in.docworkspace.com/d/sIK24hYOQApaHu7cG?sa=cl  <br>"
        "They are the faculty of MECH in 2025-26. You can also check the faculty details by clicking the link next to their name."
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
            "where did i submit my queries",
            "queries",
            "complaint"
        ],
        "answer": "You can submit your queries by using the link <br> https://docs.google.com/forms/d/e/1FAIpQLSe5kYktZG884dUGs7As2CxX240i5yq9O4pBoL4n6sJYITlRTA/viewform?usp=sf_link"
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
        "answer": "1.Dr.V.GOVINDHAN <br> https://in.docworkspace.com/d/sIDe4hYOQAs2JsbcG?sa=cl  <br>"
        "2.Mr.A.BASKARAN <br> https://in.docworkspace.com/d/sID-4hYOQApiKsbcG?sa=cl  <br>"
        "3.Mrs.KIRUBA SANDOU <br> https://in.docworkspace.com/d/sING4hYOQAquKsbcG?sa=cl <br>"
        "4.Ms.D.JASMINE SUSILA <br> https://in.docworkspace.com/d/sIDq4hYOQAuqKsbcG?sa=cl <br>"
        "5.Mrs.J.V. PESHA <br> https://in.docworkspace.com/d/sIJu4hYOQAvmKsbcG?sa=cl <br>"
        "6.Mrs.D.DHARANI <br> https://in.docworkspace.com/d/sIPm4hYOQAoOLsbcG?sa=cl <br>"
        "7.Mrs.T.SUDHA <br> ( link is not  available ) <br>"
        "They are the faculty of robotics and automation in 2025-26. You can also check the faculty details by clicking the link next to their name."
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
        "answer": "no of seats for computer science engineering in B.TECH in 2025 is... [240] and in M.TECH is ...[12]"
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
        "answer": "no of seats for electronics and communication engineering  in B.TECH in 2025 is... [180] and in M.TECH is...[12]"
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
        "answer": "no of seats for food technology  in 2025 is... [60]"
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
        "answer": "no of seats for information of things in 2025 is... [60]"
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
        "answer": "no of seats for mechanical engineering in 2025 is... [60]"
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
        "answer": "no of seats for robotics in 2025 is... [60]"
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
        "answer": "no of seats for artificial and machine learning in 2025 is... [180]"
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
        "answer": "no of seats for electrical and electronics engineering in 2025 is... [60]"
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
        "answer": "no of seats for information technology in 2025 is... [120]"
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
        "answer": "img:/static/images/vision.jpeg"
    },
    {
        "id": "College Building Image",
        "questions": [
            "college building image",
            "mvit building photo",
            "photo of college",
            "clg pic",
            "campus building picture"
            "college",
            "collage",
            "images of a clg"
        ],
        "answer": "img:/static/images/college.jpeg"
    },
    {
        "id": "Hostel Image",
        "questions": [
            "hostel image",
            "clg hostel photo",
            "show me hostel picture",
            "mvit hostel pic",
            "hostel",
            "hostal",
            "hostel in mvit",
            "boys hostel",
            "girls hostel"
        ],
        "answer": "img:/static/images/hostal.jpeg" 
    },
    {
        "id": "Sports Ground Image",
        "questions": [
            "sports ground image",
            "playground photo",
            "mvit sports pic",
            "clg ground picture"
        ],
        "answer": "img:/static/images/sports.jpg"  
    },
    {
        "id": "user intraction",
        "questions": [
            "mvit bot",
            "he bot",
            "chat bot",
            "MVIT bot",
            "mit bot"
        ],
        "answer": "yeah,Tell me, How can I hell you?"
    },
    {
        "id": "boys Hostel",
        "questions": [
            "boys hostel image",
            "boys hostel photo",
            "show me hostel picture of boy",
            "mvit boys hostel pic",
            "boys hostel",
            "boys hostal",
            "boys hostel in mvit",
            "boys hostel",
            "boys hostel"
        ],
        "answer": "img:/static/images/boys_hostel.jpeg" 
    },
    {
        "id": "girls Hostel",
        "questions": [
            "girls hostel image",
            "girls hostel photo",
            "show me hostel picture of girls",
            "mvit girls hostel pic",
            "girl hostel",
            "girls hostal",
            "girl hostel in mvit",
            "girl hostel",
            "girls hostel"
        ],
        "answer": "img:/static/images/hostal.jpeg" 
    },
    {
        "id": "PET ground",
        "questions": [
            "mvit pt ground",
            "mit pet ground",
            "MVIT p.e.t ground",
            "sports ground in mvit",
            "sports place",
            "ground"
        ],
        "answer": "img:/static/images/pet_ground.jpeg"
    },
    {
        "id": "volleyball ground",
        "questions": [
            "mvit volleyball ground",
            "mit volley ball ground",
            "MVIT volley ball ground",
            "volley ground in mvit",
            "volley ball place",
            "volleyball ground",
            "volleyball",
            "volley ball"
        ],
        "answer": "img:/static/images/volleyball_ground.jpeg"
    },
    {
        "id": "basketball ground",
        "questions": [
            "mvit Basketball ground",
            "mit basket ground",
            "MVIT basket_ball ground",
            "basket ground in mvit",
            "basket ball place",
            "basketball ground",
            "basketball",
            "basket ball"
        ],
        "answer": "img:/static/images/basketball_ground.jpeg"
    },
    {
        "id": "companies",
        "questions": [
            "no of companies in mvit clg",
            "number of company are there in mit",
            "how many companies are in mvit",
            "companies",
            "no of company"
        ],
        "answer": "MVIT has tie up with 50+ companies"
    },
    {
        "id": "companies",
        "questions": [
            "what are the companies in mvit",
            "company collab with mit",
            "some company tie up with mvit",
            "what company are partnership with mvit",
            "name the company collabrated with MVIT",
            "comapanies names",
            "company name",
            "name of the company",
            "what are the company in mvit"
        ],
        "answer": "Google,<br> Microsoft,<br> TCS,<br> Virtusa,<br> Zoho etc"
    },
    {
        "id": "no of students",
        "questions": [
            "no of students in mvit",
            "number of students studying in mvit",
            "total of students in mvit",
            "how many students are there in mvit",
            "mit students",
            "total no of students in mit"
        ],
        "answer": "MVIT currently has 3000+ students"
    },
    {
        "id":"no of labs",
        "questions": [
            "no of labs in mvit",
            "number of lab in mvit",
            "total of labs in mvit",
            "how many Lab are there in mvit",
            "mit LABS",
            "total no of labs in mit"
        ],
        "answer": "MVIT has Total 11 labs"
    },
    {
        "id":"principal",
        "questions": [
            "principal",
            "principle of mvit",
            "principal of mit",
            "who is the principal of mvit",
            "tell me the name of the principal",
            "mvit principal"
        ],
        "answer": "Dr.S.Malarkkan"
    },
    {
        "id":"trustee",
        "questions": [
            "trustee",
            "trustee of mvit",
            "truste of mit",
            "who is the trustee of mvit",
            "tell me the name of the trustee",
            "mvit trustree"
        ],
        "answer": "Mrs.V.Nirmala<br> Mrs.D.Geetha"
    },
    {
        "id":"vice chairperson",
        "questions": [
            "vice chairperson",
            "vice charperson of mvit",
            "vice charperson",
            "who is the vice chairperson of mvit",
            "tell me the name of the vicecharperson",
            "mvit vicechairperson",
            "vicechairperson"
        ],
        "answer": " Mrs.K.Nalini"
    },
    
]

# -------------------- PREPROCESS --------------------
question_to_answer = {}
all_questions = []

for entry in qa_data:
    for q in entry["questions"]:
        ql = q.lower().strip()
        question_to_answer[ql] = entry["answer"]
        all_questions.append(ql)

spell = SpellChecker()

def find_best_match(user_input):
    ui = (user_input or "").lower().strip()
    if not ui:
        return "Please type a question."
    if ui in question_to_answer:
        return question_to_answer[ui]
    match = difflib.get_close_matches(ui, all_questions, n=1, cutoff=0.70)
    if match:
        return question_to_answer[match[0]]
    return "Answer not available."

# -------------------- ROUTES --------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    data = request.get_json(force=True) or {}
    user_message = data.get('msg', '')

    words = user_message.lower().split()
    corrected_words = [spell.correction(word) for word in words]
    corrected_text = " ".join(corrected_words)

    reply = find_best_match(corrected_text)

    # If reply is an image path, return image in response
    if reply.startswith("/static/"):
        return jsonify({"reply": "Here is the picture you asked for:", "image": reply})
    else:
        return jsonify({"reply": reply, "image": None})

if __name__ == '__main__':
    app.run(debug=True)

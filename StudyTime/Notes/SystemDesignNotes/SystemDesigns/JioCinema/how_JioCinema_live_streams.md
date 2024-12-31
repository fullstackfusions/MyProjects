# How JioCinema live streams IPL to 20 million concurrent devices

source: [How JioCinema live streams IPL to 20 million concurrent devices](https://youtu.be/36N1Bz7qW0A?si=qx8WRaSvBh8jwq_p)

Here is the extracted knowledge from the conversation:

1. **IPL Overview**:

   - IPL is a significant sporting event with substantial technology and preparation ensuring smooth streaming without hiccups.
   - Prachi, a Senior Engineering Director at JioCinema, oversees discovery, personalization, and backend platform pods.

2. **Preparation for IPL**:

   - Planning starts a few months before the event, typically around November or December.
   - Includes infrastructure setup, scaling, designing fallbacks, caching across all levels, performance tuning, match day prep, and war room stories.

3. **Match Day Operations**:

   - Matches start at 7:30 PM, with war rooms activated a couple of hours before.
   - Teams, including cloud providers and payment gateways, join calls to ensure systems are green and ready.
   - Post-match debriefs are conducted to discuss any issues and improvements for the next day.

4. **Technology and Infrastructure**:

   - Use of feature flags for controlling features during live matches.
   - Simulations using tools like Charles for testing API responses and handling failures gracefully.
   - Multi-CDN strategy for load balancing and ensuring continuous service despite potential CDN issues.

5. **Database and Scaling**:

   - Detailed planning for scaling databases to handle peak loads.
   - Performance tests and audits across all systems, including front-end, CDN, load balancer, backend services, and databases.
   - Pre-scaling databases and planning capacity with cloud providers to handle expected spikes.

6. **Resilience and Mitigations**:

   - Implementation of graceful degradation strategies to handle failures without impacting the user experience.
   - Panic modes where static responses are served in case of backend failures.
   - Local storage strategies and retry mechanisms for asynchronous processing to ensure data integrity.

7. **Handling Unexpected Spikes**:

   - Buffer planning based on the expected size of the match and adjusting as the event progresses.
   - Increasing cache TTL during high load periods to reduce database load.
   - Ensuring smooth scaling down after matches in controlled steps to manage resource usage efficiently.

8. **Content Delivery Network (CDN) Strategy**:

   - Multi-CDN optimizer service to manage traffic based on CDN performance and load.
   - Continuous monitoring and switching CDNs dynamically to avoid downtime and handle traffic spikes.

9. **Ads and Personalization**:

   - Ads are a critical component, with personalized targeting based on various user segments.
   - Different methods for ad insertion, including static insertion, client-side insertion, and server-side ad insertion with personalization.

10. **Hiring and Team Dynamics**:
    - Continuous hiring across all verticals to handle the dynamic and evolving challenges of live streaming IPL.
    - Emphasis on learning and adapting to new problem statements and solutions every season.

### Conversation

सो आईpएल इज़ द बिगेस्ट स्पोर्टिंग इवेंट एंड देयर इज़ अ टन ऑफ टेक एंड प्रेप दैट गोज बिहाइंड द सींस एंस्यो ंग दैट देयर आर
नो हिक अपस वाइल स्ट्रीमिंग आईए मैचेस टू अंडरस्टैंड द साइंस आर्ट एंड इंजीनियरिंग बिहाइंड इट टुडे वी हैव प्राची विथ अस
प्राची इज़ अ सीनियर इंजीनियरिंग डायरेक्टर एट जिओ सिनेमा वयर शी लीड्स द डिस्कवरी एंड पर्सनलाइजेशन एंड बैक एंड
प्लेटफॉर्म पॉड्स एंड टुडे वी विल बी टॉकिंग ऑल थिंग्स आईपीएल राइट फ्रॉम इंफ्रा सेटअप टू स्केलिंग टू डिजाइनिंग
ऑफ़ फॉल बैक्स टू कैशिंग अक्रॉस ऑल लेवल्स परफॉर्मेंस ट्यूनिंग मैच डे प्रेप एंड वॉर रूम स्टोरीज बट बिफोर वीी जंप इन
हेलो प्राची एंड थैंक यू सो मच फॉर डूइंग दिस एंड एवरी बडी वुड लव टू नो मोर अबाउट यू सो लेट्स बिगिन विथ योर इंट्रोडक्शन
बिफोर आई आस्क माय स्टुपिड क्वेश्चंस हाय थैंक यू फॉर हैविंग मी फर्स्ट ऑफ ल इट्स रियली अमेजिंग टू बी
टॉकिंग अबाउट जिओ सिनेमा एंड ऑल ऑफ द प्रेप एंड द प्लानिंग दैट वी डू बिहाइंड
रनिंग एन इवेंट ऑफ आईपीएल स्केल सो या रियली एक्साइटेड टू बी टॉकिंग अबाउट दिस
एंड अ लिटल बिट अबाउट मी आई जॉइन जिओ सिनेमा अराउंड वन एंड हाफ यर्स बैक दिस इज द सिक्सथ आईपीएल ऑफ माय
करियर आईव आल्सो बीन पार्ट ऑफ कंपनीज हु स्ट्रीम सुपर बोल सो आईव सीन द अदर साइड
ऑफ इट एज वेल बट या रियली एक्साइटेड टूू बी टॉकिंग अबाउट ल थिंग्स आईपीएल ट सिक्स
आईपीएल इट विल बी अ फन इट विल बी अ फन डिस्कशन ओके सो लेट म स्टार्ट विथ द मोस्ट
क्लिश क्वेश्चन हाउ डज योर डे लुक लाइक बट नॉट नॉट अ यूजुअल डे बट हाउ डज र डे लुक
लाइक ड्यूरिंग एन आईपीएल मैच ओ वा टुडे इ एक्चुअली वन ऑफ दोस डे सो रियली नाइस दैट
वी आर टॉकिंग अबाउट इट अ फॉर एग्जांपल आईपीएल दिस ईयर कंसिस्ट ऑफ 74 मैचेस वन
मैच ऑन ईच डे एंड देन वी हैव टू ऑन मोस्ट वीकेंड्स अ व्हाट वी डू ऑन डे वन वर्सस
व्हाट वी डू ऑन डे 15 और डे 30 वेरीज अ लॉट अ डे वन इट लिटरली टेक्स अ विलेज टू
रन डे वन ऑफ एनी सीजन ऑफ आईपीएल बट एज अ ग्रुप व्हाट वी ट्राई टू डू इज हाउ सून
कैन वी स्विच आईपीएल टू अ बिजनेस एज यूजुअल डे वेयर ओनली अ हैंडफुल पीपल शुड
बी एबल टू रन द गेम बट या टिपिकली 7:30 पीएम इज व्हेन अ मैथ स्टार्टस अ कपल ऑफ
आर्स बिफोर दैट वी स्टार्ट आवर वर रूम्स वर रूम्स आर बेसिकली एवरी बडी जॉइन अ जूम
कॉल और इन पर्सन इफ वी आर इन ऑफिस एंड वी हैव ऑल ऑफ आवर ऑन कॉल्स वी हैव ऑल ऑफ आवर
गेम मार्शल्स वी हैव ल ऑफ आवर पार्टनर ऑन कॉल्स दैट आर पार्ट ऑफ दिस
वरूम वी हैव पार्टनर्स फ्रॉम आवर क्लाउड प्रोवाइडर्स वी हैव पार्टनर्स फ्रॉम आवर पेमेंट गेटवेज आवर सी एंड पार्टनर्स ऑल ऑफ
देम ऑन अ सिंगल कॉल अ कपल ऑफ आर्स बिफोर द मैच वी स्टार्ट स्केल अप ऑफ आवर इंफ्रा वी
बोथ कंप्यूट एंड डेटा बेसेस अ वी डू अ मेट्रिक्स रिव्यू व्हिच इज बेसिकली एवरी
टीम्स ऑन कॉल गोज थ्रू ऑल ऑफ देर डैशबोर्ड्स ऑल ऑफ देयर अलर्ट्स एंड सीज
दैट एवरी सिस्टम इज बेसिकली ग्रीन एंड गुड टू गो अ बिफोर द मैच सो वी डू अ
एक्सटेंसिव राउंड ऑफ मेट्रिक्स रिव्यू एंड देन देयर अ गेम व्हिच रंस फॉर थ्री थ एंड
हाफ आर्स एंड देन आफ्टर द मैच वी सॉर्ट ऑफ डू अ रेट्रो और अ मिनी डी ब्रीफ कॉल वेर
इफ देर र एनी इश्यूज ड्यूरिंग द गेम वी डिस्कस हाउ कैन वी डू बेटर द नेक्स्ट डे एंड व्हाट आर द थिंग्स दैट वी वांट टू
इंप्रूव ऑन सो या ट्स अ टिपिकल व एवरी डे एवरी डे ड्यूरिंग आईपीएल यू डू सो मेनी
थिंग्स या बट इ चस फ्रॉम द इवॉल्वमेंट ऑफ पीपल आवर गोल इज हैंडफुल ऑफ एंजय शुड बी
एबल टू रन इट वेर दे जस्ट अलर्ट एंड दे डोंट टू डू एनीथिंग मैनुअल टू मेक द मैच
रन ट्स द गोल दैट वी हैव एस अ ग्रुप प्रिटी प्रिटी एक्साइटिंग नाइस ओके सो यू
स्पोक अबाउट ट इट टेक्स अ विलेज टू हैंडल द डे वन ऑफ आईपीएल लाक आई जस्ट वांट टू नो
एंड आई एम शर एवरी बडी हु इज वाचिंग दिस वुड लव टू नो व्हाट हैपेंड लाइक न बेसिकली
स्पेसिफिकली टॉकिंग अबाउट दिस आईल व्हाट हैपेंड ऑन डे वन व्हाट वाज द एटमॉस्फियर लाइक इन ऑफिस व्ट ल ड यू डू लाइक एंड
ओबवियसली व्ट आईम रियली कीन टू नो इ सिंस वन डिड द प्लानिंग
स्टार्ट या सो लेट मी स्टार्ट विद डे वन दिस ईयर डे वन दिस ईयर वाज फुल ऑफ
एक्साइटमेंट एंड अ लॉट ऑफ एंटीसिपेशन ऑफ व्हाट इज गोइंग टू हैपन बिकॉज इंटरेस्टिंग
इनफ द फर्स्ट मैच दिस ईयर वाज आरसीबी वर्सस सीएसके एंड सीएसके मीनिंग धोनी एंड
धोनी मीनिंग अनप्रेसिडेंटेड स्पाइक्स एंड ट्रैफिक्स दैट एवरीबॉडी
यर एंड इट वाज देर फर्स्ट आईपीएल राइट सो ड्यूरिंग द एनटायर ईयर वन दे वर डूइंग देर
आर्किटेक्चर डिस्कशन एंड देर प्लानिंग एंड एवरीथिंग अ कपल ऑफ अस केप्ट सेइंग दैट हे
यू नो विल दिस सरवाइव योर धोनी पाइक विल दिस सरवाइव डे वन ऑफ आईपीएल सो दे हैड दिस
एनटायर बिल्ड अप इन देर माइंड एंड इट वाज देर चांस टू सी हाउ डज यो यू गेट दैट हॉकी
स्पाइक ट्रैफिक ऑन योर बैक एंड सिस्टम्स सो या फर्स्ट डे वी डिड एन इन पर्सन इन
ऑफिस वर रूम अ वी आल्सो हैड दिस लिटिल वाइट बोर्ड वेर
एवरीबॉडी
अबाउट द गेम सो या दैट वाज ओवरऑल अ डे वन ऑफ आईपीएल दिस ईयर सो व्हेन सो सिंस व्हेन
डिड द प्लानिंग स्टार्ट प्लानिंग एक्चुअली फॉर आईपीएल वी स्टार्ट अ कपल ऑफ मंथ्स
बिफोर सो इफ मार्च इज व्हेन आईपीएल स्टार्टस आ प्लानिंग स्टार्टस इन समर अराउंड नवंबर और डिसेंबर सो इट गोज इट
टेक्स अस ऑलमोस्ट थ्री फोर मंथ्स टू मेक श्यर दैट आवर सिस्टम्स आर रेजिल एनफ एंड दे आर रेडी टू हैंडल एनी सॉर्ट ऑफ स्पाइक
एनी हिक अपस यू सॉ ऑन फर्स्ट डे नो फर्स्ट डे इन फैक्ट दिस ईयर वाज द
स्मूथेस्ट आईपीएल वीव एवर सीन अ एवरी बडी हु जज डन फाइव और सिक्स आईपीएल इन आवर
ग्रुप वाज एक्चुअली सेइंग दैट दिस इ द स्मूथेस्ट आईपीएल दैट वीव सीन इन टर्म्स ऑफ स्ट्रीमिंग इन टर्म्स ऑफ द नंबर ऑफ
अलर्ट्स दैट वी गट आवर ऑन कॉल्स आवर पेजेस र रिलेटिवली मोर साइलेंट दिस ईयर एवरी एंड
आई एम शर इट ड्रीम ऑफ एवरी इंजीनियर टू बी पार्ट ऑफ सच एन एनवायरमेंट सो नाउ दैट वी
स्पोक अबाउट डे वन लेट्स टॉक अबाउट द प्रिपरेशन दैट दैट यू स्पोक अबाउट सो ईगली
माय गॉड वी डिड दिस दिस नो मोर अलर्ट लाइक वी सो द स्मूथेस्ट आईपीएल ऑन दिस वन सो ओबवियसली देर इज अ टन ऑफ प्रिपरेशन एंड
मोर इंपोर्टेंट अ टन ऑफ ऑडिट दैट गोज इन टू एश्योरिंग योर सर्विस एंड एवरीथिंग इज इन चेक सो वांट टू नो व्हाट हैपेंस
बिहाइंड द सीनस व्हेन यू जस्ट हैव टू इंश्योर एवरीथिंग इज वर्किंग फाइन लाइक वल ओबवियसली ब्रेक इट डाउन इन टू द फ्रंट एंड
बैक एंड एंड इंफ्रा बट जस्ट ऑन अ हाई लेवल ओवरव्यू साइड व्हाट डू यू थिंक इज इज
इंपोर्टेंट लाइक फॉर यू ऑल टू इंश्योर दैट एवरीथिंग रन स्मूथली या सो लाइक आई मेंशन
वी स्टार्ट आवर प्रिपरेशन अ कपल ऑफ मंथ्स बिफोर द एक्चुअल गेम द फर्स्ट स्टेप वी डू इज समथिंग दैट वी कॉल एज ऑडिट रिव्यू अ
ऑडिट रिव्यू इज नॉट डन बाय सम बडी एक्सटर्नल बट इट्स एक्चुअली ऑल ऑफ द सर्विस ओनर्स दैट गो थ्रू दिस एक्सटेंसिव
ऑडिट प्रोसेस वेर दे आर सपोज टू डिफाइन द ब्रेकिंग पॉइंट ऑफ देर सिस्टम्स एंड
ब्रेकिंग पॉइंट इज नॉट ट यो सर्व शुड स्टॉप वर्किंग राइट इट्स इट्स मोर अबाउट अवेयरनेस बिकॉज वाइल श्यर एवरी बडी फील्स
दैट यू कैन स्केल अप इनफाइनों टू वर्क विद सो द रिजल्ट ऑफ दिस
ऑडिट इज सपोज टू बी दैट बेस्ड ऑन द सीपीयू बेस्ड ऑन द मेमोरी बेस्ड ऑन योर सीडीएन
कैपेसिटी योर नेटवर्क कैपेसिटी और डेटाबेस लिमिट्स व्हाट इज द ब्रेकिंग पॉइंट ऑफ योर
सिस्टम राइट अ एंड पोस्ट दैट वी डू अ लॉट ऑफ सीरीज ऑफ परफॉर्मेंस टेस्ट लोड टेस्ट
केस टेस्ट दैट वी विल टॉक अबाउट बट या दिस इज द ओवरऑल थिंग एंड दिस ऑडिट नॉट जस्ट हैपेंस ऑन बैक एंड इट स्टार्टस फ्रॉम
फ्रंट एंड इट्स देन डन एट सीडीएन इट्स डन एट लोड बैलेंसर इट्स डन एट योर सर्विसेस
बैक देन योर डेटा बेसस सो दे लट ऑफ हॉप्स इन द रिक्वेस्ट वर्कफ्लो राट सो ल ऑफ द
हॉप्स हैव एन ऑडिट सिस्टम इन प्स आई एम जस्ट क्यूरियस लाइक बेसली सिमिलर सेट ऑफ
ऑडिट्स वड आल्सो बी डन बाय योर पार्टनर्स यस आवर पार्टनर्स एक्चुअली वी
डू द ऑडिट फॉर देम एंड देन दे डू देर ओन ऑडिट इट्स जस्ट अस इनफॉर्मिंग देम हाउ आर
वी गोइंग टू यूज दे सिस्टम इन फॉर एग्जांपल 20 मि इन गेम एंड दे नीड टू बी
इक्वली प्रिपेयर्ड इन टर्म्स ऑफ देयर इंफ्रा इन टर्म्स ऑफ देयर मिटिगेशंस सो पार्टनर ऑडिट्स आर आल्सो अ वेरी
इंपोर्टेंट पार्ट इन आवर इट डज टेक अ विलेज इट डज टेक अ विलेज इट्स नॉट जस्ट वन कंपनी इट्स नॉट जस्ट मैजिक ऑफ वन कंपनी हु
इज डूइंग इट इट इट्स द कंबाइंड एफर्ट राइ ओके लेट्स लेट्स स्टार्ट टू एक्चुअली डिग
इन फ्रॉम द फ्रंट एंड साइड एंड देन वी विल मूव टू इनफर देन टू बैक एंड सो यू स्पोक अबाउट अ लॉट ऑफ ऑडिट दैट नीड्स टू बी डन
ऑन फ्रंट एंड सो बिफोर ऑल ऑफ दिस ओबवियसली देयर शुड बी अ को कोड फ्रीज दैट यू वुड बी डूइंग और इज इट स्टिल बीइंग पोजड वाइल द
आल पल इ स्ट्रीमिंग वी डू कोड फ्रीजस एंड वी डू अ लॉट ऑफ चेंज कंट्रोल अ फ्रंट एंड
सिस्टम्स बीइंग द प्राइमरी वनस दैट गो इन टू कोड फ्रीज मच मच बिफोर ऑल ऑफ द बैक एंड
सिस्टम्स डू बिकॉज वी इफ देयर आर फॉर एग्जांपल फाइव बिल्स आउट इन द मार्केट वी नीड टू डिसाइड व्हिच इज द मोस्ट स्टेबल वन
इन टर्म्स ऑफ क्रैश फ्री सेशंस इन टर्म्स ऑफ एपीआई फेलर्स दैट आर हैपनिंग ऑन अ
पर्टिकुलर वर्जन ऑल अदर पैरामीटर्स राइट सो क्लाइंट्स एक्चुअली गो इन टू कोड फ्रीज
अ फ्यू डेज बिफोर डे वन ऑफ आईपीएल अ दैट बिल गोज टू 100% एंड देन वी स्टिल डू
कंटिन्यू शिपिंग ऑफ ऑफ प वर्जंस बट ऑफ कोर्स दे डोंट गो टू 100% वी स्टिल पुश
आउट अ लॉट ऑफ न्यू फीचर्स ड्यूरिंग द टूर्नामेंट एज वेल लेट्स स्टार्ट विद ऑडिट
ऑफ फ्रंट एंड व्हाट व्ट व्हाट हैपेंस बिहाइंड द सीनस फ्रॉम द फ्रंट एंड साइड ऑफ़ थिंग्स व्ट ल डू यू ऑडिट व्हाट ऑल डू
यू एंसर टू श लाइक डू यू डू टू एं श्योर दैट एवरीथिंग इज स्मूथ या अ सो फ्रंट एंड
ऑडिट्स द फर्स्ट थिंग दैट वी आर ह्यूज ह्यूज प्रोपोनेंट्स ऑफ फीचर फ्लैग्स अ
वाइल वन वुड थिंक दैट यू नो फीचर फ्लैग इज नॉट रियली यूजफुल और मैंडेटरी व्हेन यू
थिंक ऑफ एन आईपीएल गेम व्हिच इज स्पैन अक्रॉस लाइक थ्री थ एंड हाफ आवर्स यू डोंट
रियली हैव द लग्जरी ऑफ अ लॉट ऑफ टाइम टू बी एबल टू मिटिगेट इश्यूज सो एज अ रूल एज अ प्रैक्टिस व्हाट वी फॉलो इज एनी चेंज और
एनी फीचर दैट इज गोइंग आउट इन प्रोडक्शन इट गोज बिहाइंड अ फीचर फ्लैक एंड देन ड्यूरिंग द गेम इट हेल्प्स अस टर्न ऑफ
फीचर्स ऑन अ पर्टिकुलर प्लेटफॉर्म इफ अ फीचर इज फॉर एग्जांपल इंक्रीजिंग योर
क्रैश रेट राइट यू टर्न ऑफ दैट फीचर ऑन अ पर्टिकुलर प्लेटफॉर्म सो दीज फीचर फ्लैग्स रियली
हेल्प अस अ लॉट एंड गिव अस कंट्रोल ड्यूरिंग अ गेम टू टू मेक थिंग्स गो आवर
वे एंड टू बी एबल टू मिटिगेट इश्यूज वेरी फास्ट अ वाइल वी यूज फीचर फ्लैग्स अ लॉट
व्हाट वी डू बिफोर आईपीएल इज वी ट्राई टू सिमुलेटर दैट वड एक्चुअली हैपन इन अ लाइव
गेम वी यूज दिस टूल कॉल्ड चार्ल्स वेर वी आर एबल टू सी ऑल ऑफ द नेटवर्क रिक्वेस्ट
बीइंग मेड एंड यू कैन डू ऑल सॉर्ट्स ऑफ मोडिफिकेशंस ऑन दोज एपीआई कॉल्स सो वी सिमुलेटर लाइक एपीआई रिटर्निंग 5 एक्स
एक्स एपीआई बीइंग लेटेंट डीएनएस फेलर्स एंड एवरीथिंग दैट यू कैन इमेजिन अ बैक एंड
एपीआई टू डू न देर इ फेलर सो वी डू ल ऑफ सिमुलेशन एंड
वी सीट एवरी सिंगल एपीआई ट ब्लॉक्स द फ्लो फॉर अ यूजर ओपनिंग एन प एंड प्लेइंग द
लाइव मैच वी डू ल सर्ट्स ऑफ परमट एंड कॉमिनेशन ऑफ द फेलर ट कैन हैपन एंड मेक शर
दैट द फेलर इ नॉट रियली विजिबल टू द कस्टमर आवर गोल ए द एंड ऑफ द डे टू बी एबल
टू प्ले लाइव मैच ट द कस्टमर ज कम फर राइट सो या वी डू लॉट ऑफ फीचर फ्लैग सिमुलेशंस
अ सेकंड थिंग दैट वी डू इज वी प्लान फॉर ग्रेसफुल डि ग्रेडेशंस वाइल थिंग्स विल गो
रंग एंड एनीथिंग दैट यू फील माइट गो रंग विल गो रंग ड्यूरिंग 74 मैचेस राइट सो वी
वांट वी वांट फेलर्स टू बी नॉट विजिबल टू कस्टमर फॉर एग्जांपल व्हेन यू थिंक ऑफ योर
सिस्टम राइट देर देर आर कोर सेट ऑफ फीचर्स दैट यू थिंक ऑफ व्हिच इज एवरीथिंग दैट यू नीड टू प्ले अ लाइव स्ट्रीम देन देयर इज अ
लॉट ऑफ पीवन फीचर्स च आर ऑल ऑफ द एक्स्ट्रा लाइक तड़का दैट यू पुट ऑन योर
फीचर्स एंड देन देयर आर पीटू फीचर्स व्हिच आर लाइक इफ दे आर देयर इट्स गुड इफ दे आर नॉट देन आल्सो इट्स फाइन सो व्हाट वी
व्हाट वी डिसाइड एज अ ग्रुप इज दैट एनीथिंग दैट इज फेलिंग इन द पीव एंड प2 लेयर श्यर यू नोटिफाई र बैक एंड सिस्टम
वाय मेट्रिक्स और डेटा दैट यू आर फेलिंग बट यू डोंट रियली टेल इट टू कस्टमर बाय पुटिंग एन एरर मैसेज और सेइंग प समथिंग
वेंट रंग वच इज व्हाट वी सी इन मेनी प्रोडक्ट्स राइट सो दैट इज समथिंग दैट वी ट्राई टू डू अ लॉट अ अनदर थिंग दैट वी टेक
केयर अबाउट इज एज अ क्लाइंट इंजीनियर व्हेन आई एम कोडिंग राइट एंड आई मेक एन एपीआई इंटीग्रेशन आई सी दैट ओ सम टाइम्स
माय एपीआई इज फेलिंग आई गो एंड आई ड अ रिट्राईंग वन ट्राई आल्सो सम टाइम्स इट्स
पासिंग बट अदर टाइम्स इट्स फेलिंग सो आई गो एंड से ओ री ट्रा इनटू थ्री लेट मी ट्राई थ्री टाइम्स बट सच सॉर्ट ऑफ कोडिंग
इन अ 20 मिलियन और अबाउ गेम इट कैन एक्चुअली एंड अप टेकिंग योर सिस्टम्स डाउन
राइट अ बिकॉज यू नाउ एवरी कस्टमर इज डूइंग इनटू थ्री मल्टीप्ला बाय थ्री एपीआई कॉल्स
एंड योर सिस्टम व्हिच इज ऑलरेडी रनिंग हॉट विल एक्चुअली डाई न व्हेन यू डू थिंग्स लाइक दैट सो वी इंप्लीमेंट स्ट्रैटेजी
लाइक एक्सपो एशियल बैक ऑफ वेयर वी से दैट ओके यू पुट अ सीलिंग टू हाउ मच यू वांट टू
रिट्राईंग यू डू इट इन स्मॉल वर्स एंड दिस एक्चुअली प्रूव टू बी वेरी फ्रूटफुल फॉर
अस इन द वे वी रिक्वेस्ट लाइव वीडियोस वर यू हैव अ लिटल बिट ऑफ बफरिंग एंड यू हैव
दैट सॉर्ट ऑफ टाइम टू बी एबल टू डू एक्सपो शियल ट्राइज एक्सपोटल बैक ऑफ ट्रा सो
याट्स द आर सम ऑफ द थिंग्स दैट वी डू न क्लांट ओके ले लेट्स स्टार्ट वन बाय वन आ
आईम आईम स्लाइटली क्यूरियस अबाउट यू टॉकिंग अबाउट फीचर फ्लैग्स एंड यू बीइंग
एबल टू स्विच थिंग्स ऑन एंड ऑफ आई जस्ट वांट टू अंडरस्टैंड सम ऑफ द पैरामीटर्स इफ
यू कैन टॉक अबाउट ऑन द फीचर फ्लग लाइक ऑन बेसिस ऑफ चच यू लाइक लाक फॉर एग्जांपल मे
बी आई वांट टू टर्न दिस फीचर ऑफ फॉर लेट्स से एंड्र एंड नॉट फॉर आओ लाइक सो बेसिकली ऑपरेटिंग सिस्टम कैन बी वन ऑफ दोज
पैरामीटर्स आई रियली क्यूरिस अबाउट द परम्यूटेशंस कॉमिनेशन दैट यू कुड डू विद रिस्पेक्ट टू फीचर फ्लैग्स अ इफ यू कैन
एक्चुअली शेयर सम लाइट ऑन इट श्यर अ सो वी एक्चुअली हैव दिस इनहाउस अ सर्विस व्हिच
वी कॉल एज कन्फ सर्विस अ दिस सर्विस रिटर्न्स अ लॉट ऑफ फीचर फ्लैग्स फॉर
एवरीथिंग दैट द क्लाइंट नीड्स इन टर्म्स ऑफ फीचर फ्लैग्स राइट अ ए वर्जन इज वन ऑफ़
देम वेर इन द लेटेस्ट प वर्जन य सी समथिंग गोइंग रंग यू कैन टन ऑ फीचर फ्लग फट प
वर्जन जियोग्राफी इ वन ऑफ दोस थिंग्स इफ यू वांट टू टारगेट फीचर्स च अ लट ऑफ
पर्सनलाइजेशन टीम डज ऑन पर्टिकुलर जियोग्राफी फॉर एग्जांपल पीपल इन कर्नाटका और पीपल इन महाराष्ट्र सो जियोग्राफी इ वन
ऑफ दोस थिंग्स प्लेटफॉर्म इ वन ऑफ दोस थिंग्स सो या आर आर द टॉप थ्री फल्ट व यूज
फॉर फीचर क्ल टन ऑन एंड ऑफ आई लाइक हाउ यू क्लासिफाइड र फीचर्स टू जीरो पव आई जस्ट
आईम गेसिंग लाइक ओबवियसली योर र योर की मैथ स्ट्रीमिंग पाथ इज योर मेन क्रिटिकल
पाथ लाइक सो यूजर ओपनिंग द प टैपिंग ऑन द मैच विच इ लाइव एंड देन मैच प्लेंग दिस इज योर पी जीरो पाथ राइट एंड देन द थि दैट
गिव्स मोनेटाइजेशन ट्स आल्सो आ एड्स आई टोटली फॉग अबाउट इट बट या एड्स एड्स बीइंग
दैट सोट दैट बिकम बेसिकली दैट बम्स योर क्रिटिकल पार्ट दैट नीड्स टू बी देर देन
व्ट व्ट व्ट फीचर्स आर ए पीवन या सो इमेजिन अ कस्टमर कमिंग ऑन योर प राइट दे
ओपन द होम पेज नाउ लेट्स से दैट यू गिव द सेम वर्जन ऑफ होम पेज टू
एवरीबॉडी ग्रेडेशन सिनेरियो दैट वी विल टॉक अबाउट बट या थिंग्स लाइक दिस आर
पव नॉ रिलेटेड टू वीडियो प्ले बैक या सो सो एटंड इट्स ल अबाउट यूजर बीइंग एबल टू
सी द एड्स एंड बेसिकली वाच द मैच ट्स व्ट शुड रन एंड एंड एवरी अदर एरर यू आर जस्ट
गल्प बिकॉज यूजर शुड नॉट सी समथिंग वट र समथिंग ओके अमेजिंग नाउ द फ्रंट एंड पार्ट
प्रिटी मच सॉर्टेड वी अगेन वील बी टॉकिंग अबाउट सीडीए अ बिट मोर बट लेट्स गो न टू द
लेट्स टच अपऑन द इंफ्रा साइड ऑफ थिंग्स ब बडी इज क्यूरियस लाइक 20 मिलियन स्केल एंड दिस दैट एंड हाउ इज र इंफ्रा टेकिंग दोस
थिंग्स अप सो गिवन दैट ओके लेट्स लेट मी जस्ट पुट बेसिकली
वेरी ब्रॉडर क्वेश्चन एंड देन वी कैन डाइव डीपर हाउ डू यू ऑडिट योर बैक एंड इंफ्रा टू एंसर दैट एवरीथिंग रन स्मूथ सो वी
स्पोक वेरी इन डेप्थ अबाउट द फ्रंट एंड साइ ऑफ थ लेट्स टच अपऑन द इंफ्रा साइड या
सो लेट्स से वी ट्रेस अ सिंपल रिक्वेस्ट फ्लो राइट योर क्लाइंट सेंडस अ रिक्वेस्ट इट गोज टू वन ऑफ आ सीडी वी ड मल्टी सीडीएन
सो इट्स नॉट अ सिंगल सीडीएन मल्टीपल सीडीएस दैट वी अ यूज एंड देन फ्रॉम योर
सीडीएन इट कम्स टू योर लोड बैलेंसर फ्रॉम लोड बैलेंसर इट गोज टू योर ओरिजिन सर्वर्स
एंड देन इट गोज टू योर डेटा बेसस दिस इज हाउ अ टिपिकल रिक्वेस्ट प्रो वुड लुक लाइक
इफ वी स्टार्ट फ्रॉम द राइट हैंड साइड व्हिच इज फ्रॉम योर डेटा बेसेस राइट डेटा बेसेस आर द मोस्ट डिफिकल्ट अ स्केलिंग
फैक्टर्स और प्रॉब्लम स्टेटमेंट व्हेन इट कम्स टू स्केलिंग राइट बिकॉज अ
आई थिंक मोस्ट ऑफ द पीपल आव स्पोकन टू हु हैव नॉट वर्क्ड इन आईपीएल द फर्स्ट तुक्का
सर्ट ऑफ दैट कम्स हे इट्स ऑटो स्केलिंग राइट वेरी इजी जस्ट डू दैट चेक मार्क ऑन
योर क्लाउड प्रोवाइडर एंड थ शस्ट ऑटो स्केल बट इन रियलिटी इ डजन वर्क दैट वे बिकॉज ऑफ अ लट ऑफ पैरामीटर्स
वन इट टेक्स अ लॉट ऑफ टाइम फॉर ऑटो स्केलिंग टू ट्रिगर व्हेन यू हैव अ थथ एंड हाफ आ गेम इफ यो ऑटो स्केलिंग इ टेकिंग
एनीवे फ्रॉम कपल ऑफ मिनट्स टू एन आर टू ऑटो स्केल ट्स लाइक हाफ ऑफ योर गेम गन एंड
दैट आल्सो लीड्स टू अ लॉट ऑफ मॉनेटरी इंपैक्ट फॉर अस राइट जस्ट टू गिव यू एन इंस्टेंस लास्ट ईयर वी हैड एन इवेंट वेयर
वी गट अ स्पाइक दैट वी वर नॉट एंटीसिपेटिंग फॉर इट वाज नॉट इवन आईपीएल अ
डिफरेंट सीरीज एंड वी सॉ वन ऑफ आवर डेटा बेसेस हैड रीच 100% सीपीयू थ्रश होल्ड एंड
वी स्टार्टेड द स्केल अप एंड इट टूक अस 45 मिनट्स टू बी एबल टू जस्ट ड फाइव नोट्स टू
इट एंड हाफ ऑफ द गेम वाज ओवर बाय देन सो ऑटो स्केलिंग डजन वर्क फॉर अस वी नीड टू
स्केल अप आवर डेटा बेसेस मच मच बिफोर द गेम नाउ हाउ डू वी प्लान फॉर इट इज एन
एनटायर डिफरेंट प्रॉब्लम स्टेटमेंट राइट द फर्स्ट थिंग दैट वी डू इज वी डू बैक ऑफ द एनवेलप कैलकुलेशन च इज बेसिकली एवरी बैक
एंड सिस्टम ओनर दे स्टार्ट विथ वन पड वन कुबस पॉड एंड दे से दैट ओके वन पॉड इफ आई
एबल इफ आई हैव टू बी समवेल एंड मेमोरी बेस्ड ऑन व इफ यू हैव
लोकल कैश और यू डोंट आई वांट टू स्टे इन द सेफ रेंज एंड आई वांट माय एपीआई टू रेस्पों इन फ्यू मिली सेकंड्स एंड देन वी
से ओके इफ वी आर सेइंग देस अ 20 मिलियन कॉन्करेंस गेम एंड फॉर 20 मिलियन कॉन
करेंसी हाउ मेनी रिक्वेस्ट विल योर एपीआई गेट आफ्टर ऑल ऑफ योर सीडी एन कैसेस एंड ऑल ऑफ दैट हाउ मेनी रिक्वेस्ट कम्स ऑन योर
ओरिजिन एंड हाउ मेनी रिक्वेस्ट फॉर वन क्लाइंट रिक्वेस्ट गोज टू योर डेटाबेस फॉर
एग्जांपल वन क्लाइंट रिक्वेस्ट कैन कैन डू लाइक थ्री डीबी कॉल्स राइट सो देन वी
स्टार्ट डूइंग दस कैलकुलेशन दैट ओके इफ दज आर द नंबर ऑफ रिक्वेस्ट दैट आर कमिंग ऑन माय ओरिजिन देन आई विल गेट दज मेनी
डेटाबेस कॉल्स फॉर मी टू बी एबल टू रेस्पों इन लाइक अ 60 पर सीपीयू यूटिलाइजेशन कंसीडरिंग वील हैड सम बफर्स
एंड इन दिस मच लेटेंसी दैट वी आर कंफर्टेबल विद दीज आर द नंबर ऑफ नोड्स एंड द साइज ऑफ न ट आ नी एंड
देन वी प्री स्केल एंड कीप इट बिफोर द गेम बिकॉज आल्सो गेटिंग दैट मच कैपेसिटी फ्रॉम
अ क्लाउड प्रोवाइडर इ नॉट रियली इजी राइट सम टाइम्स वी एंड अप टेकिंग 75 पर ऑफ
इंडिया इंटरनेट बैंडविथ अवेलेबल सो इट्स नॉट रियली इजी टू जस्ट गो टू क्लाउड
प्रोवाइडर एंड से हे गिव अस सस मेनी मोर नोट्स क्लाउड प्रोवाइडर आल्सो नीड टू प्लान अ लट विथ अस इन एडवांस ट हाउ मच
कैपेसिटी वी आर गोइंग टू टेक फम सो या दिस इ अ लिटिल बिट अबाउट हाउ वी डू प्लानिंग ऑन डेटाबेस केलिंग एंड एंड आई ऑलवेज से
दिस लाइक डेटाबेस इज द मोस्ट ब्रिटल कंपोनेंट ऑफ़ आर आर्किटेक्चर इफ इट गोज डाउन एवरीथिंग इज डाउन सो ऑल यू डू इज
जस्ट एं श्योर दैट यो डेटाबेस इज अप एंड रनिंग नो मैटर व्हाट राट सो अगेन लाइक वन
वन वन क्वेश्चन दैट आई हैव फॉर यू ऑन दिस व्हेन यू आर टॉकिंग अबाउट द बैक ऑफ़ द नवल अप कैलकुलेशन सो फॉर वन कुबर टस पॉड टू सी
दैट इफ इट वांट्स टू ऑपरेट एट बेसिकली 60 पर ऑफ कैपेसिटी ऑन द डेटाबेस द ओनली वे फॉर यू टू डू दिस इज लो टेस्ट और इज देयर
अ मैजिक इज देयर अ मैजिक फार्मूला दैट यू यूज नो सडली देर इज नो मैजिक फार्मूला दैट
वी हैव बिकॉज एवरी एपीआई एंड एवरी एंड पॉइंट इन द सर्विस गेट्स डिफरेंट अमाउंट
ऑफ ट्रैफिक फॉर द सेम कॉन्करंसी नंबर बिकॉज ऑफ वेयर दे आर प्लेस इन द एप फॉर एग्जांपल व्हेन धोनी कम्स वाइल पीपल आर
डिस्ट्रीब्यूटर इन द वे दैट दे कम ऑन द एप इन अ स्पैन ऑफ लाइक फाइव मिनट्स इट्स द प्लेबैक सिस्टम एंड द प्लेबैक एपीआई दैट
गेट दैट स्पाइक बट व्हेन धोनी गेट्स आउट इट्स एक्चुअली ऑल ऑफ द एपीआई ऑन द होम पेज
बिकॉज एवरीबॉडी
गेट्स आउट ऑल ऑफ आवर सिस्टम्स गेट दैट हॉकी स्पाइक अ ट्रैफिक ऑन ऑल ऑफ आवर होम
पेज एपीआई सो देर इज नो वन फार्मूला फिट्स ऑल अ एंड आफ्टर ऑल दिस प्लानिंग आल्सो
थिंग्स विल गो बैड राइट योर सीपीयूज विल स्पाइक एंड हाउ यू प्लान टू हैंडल दैट अ
इज समथिंग दैट आई आल्सो वांटे टू टॉक अबाउट सो वन ऑफ द थिंग्स वी डू एज
मिटिगेशंस इज टू सी कैन यू इंक्रीज द टीटीएल ऑफ द कैसेस अ दैट आर इन फ्रंट ऑफ योर डेटा बेसेस सो दैट वुड रिड्यूस अ
लिटिल बिट ऑफ लोड ऑन योर डेटाबेस एंड गिव इट टाइम टू कल ओवर बट पीपल विल गेट अ
स्टेल रिस्पांस बाय अ कपल ऑफ मिनट्स व्हिच माइट बी ओके फॉर सम यूज केसेस राइट अ सम टाइम्स इट हेल्प्स सम टाइम्स इट डजन
योर डेटा बेसेस कैन स्टिल गो डाउन राइट एंड व्ट वी डू इन दोज केसेस इज वी प्लान फॉर सिनेरियो लाइक दिस एंड वी कॉल इट
पैनिक मोड्स व्हिच इज बेसिकली इमेजिन योर हाउसेज ऑन फायर नाउ कस्टमर ऑफ कोर्स कैन
नॉट नो दैट राइट यू कांट जस्ट नॉट स्ट्रीम लाइव मैचेस फॉर देम सो व्हाट वी डू इज बिफोर द मैच वी टेक अ स्नैपशॉट ऑफ व्हाट
योर एपीआई रिस्पांस वुड हैव लुक्ड लाइक एंड वी टेक दैट स्नैपशॉट एंड वी पुट इट इन अ स्टैटिक स्टोरेज एंड वी कीप दोस रेडी
एंड ऑल ऑफ दिस इज ऑटोमेटेड राइट सो ऑफ कोर्स मोस्ट एपीआई लाइक योर पला एी वि पर
यूजर यू कां डू ट बट मोस्ट ऑफ आवर एपीआई लाइक योर कैटलॉग और यो प्लेबैक वी कैन डू
दिस एंड वी पुट दिस न स्टैटिक स्टोरेज वेन समथिंग गोज रंग वी जस्ट स्विच आवर सीडीएन
टू नॉट टॉक टू आवर ओरिजिन एंड टॉक टू द स्टैटिक स्टोरेज एंड लास्ट यर आईपीएल वन
ऑफ माय सिस्टम एक्चुअली हैड सम इशू ड्यूरिंग द मैच एंड वी हैड टर्न ऑन दिस
पैनिक मोड एंड न वी डूइंग द डी ब्रीफ आफ्टर मैच वी रिलाइज फ्रॉम आवर कस्टमर सपोर्ट टीम दैट देर वार जीरो कंप्लेंट्स
अबाउट द सिस्टम गोइंग इन टू पैनिक मोड बिकॉज इट वाज नॉट विजिबल टू द कस्टमर आई
मीन वी टर्न ऑफ अ लिटिल बिट ऑफ पर्सनलाइजेशन वी सेंट अ स्टैटिक रिस्पांस द मैच वाज देयर पीपल कुड गो टू द मैच एंड
वाच द गेम सो पैनिक मोड्स रियली आई थिंक हेल्प अस अ लॉट वी यूज इट एक्सटेंसिवली इन
द वे दैट वी क्रिएट ऑटोमेशंस फॉर इट लकली नफ वी जस्ट होप दैट वी डोंट हैव ट टर्न इट ऑन बट या इट्स लवेज देयर टू सेव अस वन द
डे इज बैड इट लुक्स लाइक लाइक लाइक एवरी सिंगल डिजाइन डिसिजन टट यू फोक्स आर
टेकिंग इट्स लवेज अबाउट हैविंग अ प्लान बी रेडी ट्स ट्रू प्लान बी सी
डी ट्रू ऑन द ऑन द डेटाबेस साइड यू र टॉकिंग अबाउट सर्जेस लाइक यू यू गेट एन
अनएक्सपेक्टेड स्पाइक एंड लेट्स से यू प्रोविजन अ सर्टेन कैपेसिटी एंड यू स्टिल
यू स्टिल गट द स्पाइक एंड यू आर अनेबल टू हैंडल व्हाट व्हाट हैपेंस देन लाइक से थ द मैच इ लाइव स्पाइक हैपन हाउ डू यू रिएक्ट
या फर्स्ट इज टू हैव इनफ बफर एंड नोइंग व्हाट मैच यू आर हैविंग टुडे राइट फॉर एग्जांपल इफ यू आर हैविंग आरसीबी वर्सस
सीएसके और यू आर हैविंग ए वर्सस सीएसके दीज गेम्स आर रिलेटिवली बिगर देन फ्यू ऑफ
द अदर मैचेस राइट सो हैविंग अ बफर दैट यू आर कंफर्टेबल विद एंड एट द सेम टाइम नॉट
स्पेंडिंग अ लॉट ऑफ मनी दैट इज समथिंग दैट दैट नीड्स अ लॉट ऑफ ट्यूनिंग एंड मे बी ऑन
डे वन और डे टू यू टेक अ लिटिल बिट ऑफ एक्स्ट्रा बफर बट एज द इवेंट प्रोग्रेसेस
यू फाइंड ट्यून दोस थिंग्स एंड यू कम टू अ स्वीट स्पॉट वेयर यू विल बी एबल टू सरवाइव
लाइक अ 2 एक्स पाइक देन व्हाट यू रिसीवड ऑन द प्रीवियस डे एंड देन यू स्केल डाउन
योर सिस्टम्स आफ्टर द मैच सो आई थिंक प्लानिंग इज ऑल वी डू एंड देन स्टिल इफ यूर डेटाबेस हैज अ स्पाइक और गोज टू 100%
सीपीयू वी स्पोक अबाउट इट यू ट्यून योर कैश यू इंक्रीज द कैश टीएल एंड या थिंग्स
लाइक दैट डू यू डू समथिंग डिफरेंट इन टर्म्स ऑफ स्केलिंग डाउन या सो वी डोंट
रियली स्केल डाउन ड्यूरिंग द मैच वाइल धोनी हैज प्लेड एंड ज इज आउट एंड इज डूइंग
सम एंड सम अदर प्लेयर इज प्लेइंग राइट ही माइट स्टिल कम बैक फॉर हिज बलिंग और विकेट
कीपरिंग एंड यू विल गेट द स्पाइक्स अगेन और इफ देर समथिंग रियली एक्साइटिंग हैपनिंग इन द मैच यू गेट योर स्पाइक अगेन
सो वी डोंट रियली स्केल डाउन ड्यूरिंग अ मैच वी स्केल डाउन आफ्टर द मैच एंड आफ्टर
द मैच आल्सो वी डोंट डायरेक्टली गो फ्रॉम लाइक अ 20 30 मिलियन लैडर टू लाइक से अ टू
टू थ मिलियन लैडर देर आ स्टिल मिलियंस ऑफ पीपल हु स्टे बैक ऑन द प्लेटफॉर्म आफ्टर द मैच इज ओवर एंड दे वाच देयर फेवरेट अदर
ओडी शोज और सम अदर लाइव स्ट्रीम सो व्हाट वी डू इज वी स्केल डाउन इन लैडर्स एंड दैट
लैडर अगेन डिपेंड्स ऑन द नंबर ऑफ कस्टमर्स दैट आर ऑन द प्लेटफॉर्म एट अ गिवन टाइम सम
टाइम्स इट्स अ 5 मिलियन लैडर स्टेप डाउन सम टाइम्स इट्स अटू मि लटन सम टाइम्स इट्स लाइक अ इवेंट डूइंग इट लाइक वेरी स्लोली
वेरी या सो स्केल डाउन अगेन हैज इट्स ओन टिप्स एंड ट्रिक्स अ योर रिक्वेस्ट कैन गो
टू पॉड्स व्हिच आर इन डिग्रेडेशन मोड सो यू डू लाइवलीनेस चेक्स रेडनेस प्रोब्स एंड थिंग्स लाइक दैट अ टू ट्यून दोस
पैरामीटर्स ऑल ऑफ द बैक एंड सर्विसेस नीड टू हैव ग्रेसफुल डिग्रेडेशन अगेन वेर दे नोटिफाई दैट ओके आई एम नॉट एक्सेप्टिंग
एनी रिक्वेस्ट नाउ डोंट सेंड मी एनी रिक्वेस्ट एंड देन द व शट डाउन सो या
स्केल डाउन इ आल्सो अ बिट ट्रिकी एवरीथिंग इज ट्रिकी एट स्केल टॉ या ब बट आई लाइक
दैट अप्रोच बेसिकली यू हैव अ टच मी नॉट पॉलिसी ड्यूरिंग द मैच व्हाट एवर इ कॉन्फिन फिगरड डोंट टच एनीथिंग इट्स
वर्किंग इवन इफ वी लीक अ बिट ऑफ मनी ड्यूरिंग दैट थ फोर आर स्पैन इट्स ओके बट
अगेन बिकॉज ट्स द हार्ट एंड सोल ऑफ एवरीथिंग दैट यू फोक्स टू इंटरेस्टिंग ना
आई जस्ट वांट टू टच अपऑन अ अ बिट ऑफ डिटेल्स ऑन दिस लाइक व्हाई मल्टी सीडीए
नंबर वन एंड हाउ डज योर फ्रंट एंड नो व्हिच सीडीएन टू टॉक टू लाइक लाइक डू यू
स्विच इट ऑन द फ्लाई अ या अ सो मल्टी सीडीएन व्हाई डू वी यूज इट बिकॉज ऑफ कोर्स
यू वुडन वांट टू रिलाई ऑन अ सिंगल सीडीएन आल्सो सीडीएस हैव देयर ओन लिमिट्स इन टर्म्स ऑफ हाउ मेनी कपेस एज सर्वर्स कैन
दे हैव एंड व्हाट इज देयर कैपेसिटी दे आर नॉट सम मैजिक पोशंस दैट कैन यू नो जस्ट
सॉल्व एवरीथिंग दे आर आल्सो एट द एंड ऑफ द डे दे आल्सो हैव देर फिक्स अमाउंट ऑफ सीपीयू फिक्स अमाउंट ऑफ मेमोरी एंड द
अमाउंट ऑफ ट्रैफिक दैट वी कैन डू सो हाउ डू यू ट्यून च ट्रैफिक गोज टू विच सीडीएन
इज वी हैव अ सिस्टम कॉल्ड मल्टी सीडीएन ऑप्टिमाइजर च डज दिस इट डिसाइड्स बेस्ड ऑन
हाउ हॉट सीडीएन इज रनिंग वेर टू सेंड द ट्रैफिक एंड वी मेजर यूज दिस फॉर आवर लाइव स्ट्रीमिंग राइट वी हैव मल्टीपल सीडी दैट
वी वर्क विद अगेन ऑन सी देर अ फेयर बिट ऑफ ट्यूनिंग्स एंड प्लानिंग दैट वी नीड टू डू
अ द फर्स्ट वन बीइंग कैश ऑफ लोडस राइट अ एवरी बैक एंड इंजीनियर आई एम शर वुड ऑलवेज
थिंक हे आई वांट ऑल ऑफ द रिक्वेस्ट टू कम टू माय ओरिजिन बिकॉज आई वान दिस न मिलियन
ट्रांजैक्शन पर सेकंड सॉर्ट ऑफ सिस्टम बट आई थिंक इन आवर कंपनी द रियल इंजीनियरिंग
कम्स व्हेन योर कैश ऑफ लोड इज लेस देन 90 पर द वे यू डिजाइन योर कैसेस एंड य द वे
यू डिजाइन व्हाट विल बी योर कैश कैशिंग पॉलिसी एट सीडीएन दैट इज एक्चुअली द रियल
इंजीनियरिंग यूर सपोज टू ऑफ लोड मोस्ट ऑफ द थिंग्स ऑन सीडीएन बिकॉज इ इट आल्सो
डिपेंड्स ऑन अ लॉट ऑफ मनी दैट यू आर स्पेंडिंग न देर ज न मिलियन रिक्वेस्ट कमिंग देर ल गोइंग टू र डेटाबेस सो यू
पेइंग टू द डेटाबेस यू पेइंग टू योर कंप्यूट एंड देन यू पेइंग टू सीडीएन आल्सो सो कैश ऑफ लोड इज वन थिंग दैट दैट वी
रियली मॉनिटर अ लॉट ल ऑफ द पर्सनलाइजेशन एपीआई फॉर एग्जांपल कैन नॉट बी कैश बिकॉज
दे आर पर यूजर बट एवरीथिंग एल्स व्हिच कैन बी कैश हैव टू बी कैश अ सो कैश ऑफ लोड इज
वन ऑफ दोज थिंग्स अ वन ऑफ द इंटरेस्टिंग प्रॉब्लम स्टेटमेंट्स दैट वी हैड दिस ईयर
वाज वी हैव थ्री स्टैक्स ऑन सीडीएस राइट वी हैव योर वीडियो स्टैक यू हैव योर एपीआई स्टैक एंड देन यू हैव योर इमेज स्टैक नाउ
अ कपल ऑफ डेज इन टू द आईपीएल वी र ऑल मॉनिटरिंग आवर वीडियो एंड एपीआई स्टैक एंड वन ऑफ आवर सीडीएन पार्टनर्स सेड हे देर
समथिंग रॉन्ग गोइंग ऑन न योर इमेज स्टैक एंड इट हैज टच 90 पर सीपीयू एंड वी वर ऑल
रियली कंफ्यूज वी र लाइक इमेजेस इज रियली जस्ट स्टैटिक डिलीवरी लाइक व्हाट कुड बी गोइंग रंग देयर एंड इफ इमेजेस गोज डाउन
देर लिटरली नथिंग लेफ्ट ऑन आवर प बिकॉज यू ओपन द होम पेज वी जस्ट हैव मूवी पोस्टर्स
एंड शो पोस्टर्स वी डोंट हैव एनी टेक्स्ट सो दैट वाज रियली लाइक अ पी जीरो सॉर्ट ऑफ इंसिडेंट फॉर अस व्हाट वी डिड ड्यूरिंग
दैट टाइम इज वी वेंट एंड वी सो द ट्रैफिक ऑन आवर सीडीएन फॉर द इमेज रिक्वेस्ट एंड
वी स दैट देर वाज अ सेट ऑफ 30 टू 50 इमेजेस दैट र डूइंग न मिलियन आरपीएस ऑन आ
सीडीएन एंड वी र लाइक ओके व्हाट आर दिस इमेजेस एंड वी रिलाइज दैट वी हैड लच दिस
फीचर दिस यर कॉल्ड स्टर्स वेर यू गो टू द प्लेबैक पेज एंड यू सी स्टर्स ऑफ योर
फेवरेट टीम्स और योर फेवरेट क्रिकेटर्स एंड देर र 50 स्टिकर मे बी पर गेम दैट वन
कस्टमर रिक्वेस्ट वास ट्रांसलेटिंग टू 50 इमेजेस बीइंग डाउनलोडेड फ्रॉम द सीडीएन
एंड दैट वाज जस्ट लाइक बर्डिंग आवर सीडीएन राइट सो व्हाट वी डिड फर्स्ट स्टेप जज
मिटिगेशन वाज दैट वी सेड ओके कैन वी इंक्रीज द डीटेल ऑफ दोस इमेजेस सो दैट पीपल हु हैव रिसीवड इट वंस व्हेन दे कम
बैक इट्स लोडेड फ्रॉम देर डिवाइस कैसेस एंड डजन रियली एंड अप कमिंग टू सीडीएन दैट
हेल्प अस अ बिट बट देन अगेन फ वी हैव अ लॉट ऑफ न्यू पीपल दैट कम ऑन द प्लेटफॉर्म
राइट सो व्हाट वी डिड वाज वी र लाइक ओके वी हैव टू ऑप्शन वन इज यू डू स्प्राइट एंड
द सेकंड थिंग इज यू डू बेस 64 एंड लकली बिकॉज दज इमेजेस आर शेरेबल ऑन द स्टर्स वी
ऑलरेडी हैड बेस 64 एन कोडेड वर्जस ऑफ दिस प्रेजेंट सो वी बंडल देम टुगेदर एंड सेंट
टू क्लाइंट्स इन वन सिंगल एपीआई कॉलन दैट गट आवर आरपीएस फ्रॉम लाइक 10 मिलियन
आरपीएस टू 100 के आरपीएस सो दे लट ऑफ ट्यूनिंग दैट यू नीड टू डू एट सीडीएन एज
वेल इट डजन जस्ट इट डजन वर्क आउट ऑफ द बॉक्स सो या या अ लट ऑफ पीपल एक्चु य थिंग
दैट सीडीएन डज ऑल द मैजिक एंड देर इज अ वेरी लाइक लाक एवरी बडी जस्ट टॉक अबाउट हे दीज गाइज आर नॉट डूइंग एनीथिंग इट्स ऑल
दिस बट बट बेसिकली टॉकिंग विद यू ऑन दिस टॉपिक यू लाइक आई एम रियली हैप्पी दैट नाउ
पीपल वुड अंडरस्टैंड लाइक इवन दस स्मल थिंग व्हिच इज नॉट स्मल लाइक लाइक इट्स जस्ट अ स्टिकर फॉर यू इट इज जस्ट अ स्टिकर
बट फॉर द कंपनी हु इज सर्विंग इट द सीडीएन हु इज सर्विंग इट इट्स लॉट मोर एंड एंड
जस्ट जस्ट जस्ट वन थिंग ऑन द मल्टी स्न पार्ट हाउ हाउ ऑन द फ्लाई हाउ डू स्विच बिटवीन सी य यू से दैट यू हैव दैट बेसिकली
मल्टी सीडीएन ऑप्टिमाइजर सर्वेस बट डज योर फ्रंट एंड मेक अ कॉल टू बैक एंड टू अंडरस्टैंड वयर टू सेंड अ रिक्वेस्ट टू और
हाउ डज दैट वर्क नो आर बैक एंड डिसाइड्स एंड सेज दैट दिस इज योर यूआरएल वेर यू आर सपोज टू गेट द रिक्वेस्ट फ्रॉम सॉरी गेट द
रिस्पांस फ्रॉम एंड बैक एंड डज ऑल ऑफ द ट्यूनिंग दैट हाउ मेनी रिक्वेस्ट टू सर्व टू अ पर्टिकुलर सीडी सो डज दिस चेंज लाइक
हाउ फ्रीक्वेंसी अ कपल ऑफ मिनट्स टू अ फ्यू आर्स बेस्ड ऑन
हाउ हॉट अगेन अ सीडीएन इज रनिंग एंड इट डज हैपन डरिंग द मैच वे वन ऑफ आवर सीडीएन पार्टनर्स इफ देर समथिंग गोइंग रंग ऑन वन
ऑफ देर ए सर्वर्स दे कम एंड नोटिफाई अस दैट हे यू नो एन ए सर्वर इन फॉर एग्जांपल महाराष्ट्र इज हैविंग इशू सो नाउ वी नो
दैट रिक्वेस्ट कमिंग फ्रॉम महाराष्ट्र लेट अस नॉट सेंड टू द सीडीएन बिकॉज वी नो द सर्वर इज डाउन लेट अस सेंड इट समर एल्स सो
ड सीडीएन ऑप्टिमाइजर सर्विस टेक इनटू कंसीडरेशन दिस पैरामीटर्स एंड देन डिसाइड
ओके सो वन थिंग आव ऑलवेज हर्ड एंड अगेन इ इवन इवन आई फॉलो व्हेन एवर आई डिजाइन द
सिस्टम दैट थिंग्स दैट नीड नॉट बी डन इन रियल टाइम शुड नॉट बी डन इन रियल टाइम व्हिच मींस देर वुड बी अ टन ऑफ सिंक्रोनस
अ जॉब्स दैट वुड बी प्रोसेस्ड और लेट्स से योर रिएक्शंस और द चैट्स दैट वुड गो लाइक
लेट्स जस्ट टॉक अ बिट अबाउट ऑल सॉर्ट्स ऑफ असंक्रामक
आवर काफ का सिस्टम इ स्ट्रक्चर्ड इज दैट द ऑनबोर्डिंग इज सॉर्ट ऑफ लाइक वेयर यू
रिव्यू ऑल ऑफ र यूज केसेस वी वी डोंट रियली डू दैट ओके देर अ काफ का हियर कम
एंड यूज इट देर अ लॉट ऑफ प्लानिंग दैट हैपेंस व्हेन यू ऑन बोर्ड अ यूज केस ऑन काफ का राइट देयर इज देर आर पैरामीटर्स
लाइक हाउ मच थ्रू पुट इन गीगाबाइट पर सेकंड विल यू डू व्हाट इज योर प्रोड्यूसर रेट व्हाट इज योर कंज्यूमर रेट वी प्लान
आवर पार्टिस बेस्ड ऑन दैट आफ्टर ऑल ऑफ दीज थिंग्स आर डन देर आर स्टिल केसेस वेयर यू
नो देर विल बी अ लॉट ऑफ बैकअप दैट हैज बीन बिल्ट सो वी इंप्लीमेंट स्ट्रेटेजी लाइक
कैन यू पुट द डेटा इन अ लोकल स्टोरेज एंड देन प्रोसेस इट लेटर आफ्टर द मैच बिकॉज ऑफ
कोर्स यू कांट लूज योर डेटा राइट एंड इफ काफ्का इज रनिंग ट कैन यू स्टॉप योर
कंज्यूमर्स अ टू मेक एंड क्रिएट मोर स्पेस फॉर अदर यूज केसेस सो अगेन आई थिंक देयर ज
अ लॉट ऑफ ट्रेड ऑफस दैट वी डू पी जीरो यूज केसेस आर ऑलवेज प्रायोरिटी अ एंड पीव एंड
पीट कैन वेट एंड प्रोसेस देर डेटा आफ्टर द मैथ सो अगेन बिल्डिंग दोस टॉगल्स एंड हैविंग दैट कंट्रोल हेल्प्स अस अ लॉट
व्हेन इट कम्स टू मेसेजिंग सिस्टम्स अ एनी स्पेसिफिक एग्जांपल ऑन योर
मैसेजिंग सिस्टम लाक इन केस लेट्स से योर प्राइमरी काफ क्लस्टर इज डाउन हैज इट एवर
हैपेंड लाइक ड्यूरिंग अ मैच योर योर प्राइमरी सिंक्रोनस प्रोसेसिंग क्यू इज
डाउन इन दैट केस व्हाट डू यू डू सो यू यू स्पोक अबाउट वन ऑफ द वेज टू डू इट सो लेट्स से योर एपीआई सर्वर्स व्हेन दे आर
पुशिंग टू काफ का लेट्स से काफ्का इज डाउन दे स्टोर इट लोकली सो
फोर्चुनेगीएंट्स
दैट इज प्रायरिटाइज फॉर एग्जांपल द व्यू काउंटर दैट यू सी ऑन टॉप ऑफ द प्लेयर राइट
ऑन टॉप राइट दैट इज एक्चुअली यूजिंग काफ्का एज द प्राइमरी सिस्टम सो फॉर दैट
टू वर्क ऑफ कोर्स इट कैन बी इवें कंसिस्टेंट इटस नोबडी नीड्स टू नो द एज्ट लाइक 2.4 डेसीमल
नंबर ऑफ पीपल ट देयर बट एनीथिंग दैट इज नीडेड फॉर द क्लाइंट एप्स टू रन दैट टेक्स
प्रायोरिटी ऑल आ द सिस्टम्स वी टर्न ऑफ द टॉगल्स लाइक आई सेड वी प्रोसेस इट आफ्टर द मैच न देर नॉट मच
ट्रैफिक ए वन थिंग दैट आईव सीन एस पैटर्न इट्स मोर अबाउट यूजर बिहेवियर
अंडरस्टैंडिंग न रिक्वायर्स ऑन द व्ट लाइक हाउ योर एंड यूजर इज गोइंग टू यूज द प एंड
देन यू जस्ट इंश्योर दैट दैट हैप्पी पाथ इज वर्किंग फाइन नो मैटर व्हाट राइट करेक्ट एनी लाइक ओबवियसली देयर वुड बी अ
टन ऑफ स्टोरीज यू आर इन योर सिक्स्थ आईपीएल एनी फन वॉर टाइम एनी फन आउटेज
स्टोरीज दैट दैट दैट यू माइट वांट टू शेयर या आई थिंक देर वाज वन अ कपल ऑफ डेज
बिफोर आईपी वेर आवर कस्टमर सपोर्ट टीम रीड आउट टू अस एंड सेड हे वी आर गेटिंग कंप्लेंट्स ऑफ फ्यू पीपल नॉट अ बीइंग एबल
टू ओपन द पप एंड वी वर लाइक ओके
दैट्ची चेक देयर इंटरनेट कनेक्शंस इंडिया में लाइक मोस्ट ऑफ द टाइम्स व्हाट टर्न्स आउट इज दैट द इंटरनेट कनेक्शन वाज बैड बट
देन अ द पर्सन फ्रॉम आवर कस्टमर सपोर्ट टीम सेड इट्स ओनली जिओसिनेमा ए दैट इट्स नॉट ओपनिंग सो इट्स लिटरली समथिंग टू डू
विथ अस राइट एंड देन वी स्टार्टेड ट्रेसिंग दोज रिक्वेस्ट टू फिगर आउट वेर एक्चुअली इट फेल्ड एंड वी स्टार्टेड फ्रॉम
आवर सीडीएन पार्टनर्स टू आवर लोड बैलेंसर्स बैक इन सिस्टम एंड वी र सीइंग एवरीथिंग लाइक नथिंग गोइंग रंग राइट एंड
देन लकली वन ऑफ आवर कॉलीग सेड दैट यू नो व्हाट आई एम एबल टू रीप्रोड्यूस दिस एंड
नॉट जस्ट मी माय एनटायर बिल्डिंग इज नॉट एबल टू ओपन जियो सिनेमा एंड ट्स व्हेन वी रिलाइज दैट यू नो दिस वाज समथिंग डिफरेंट
एंड अ बिग इशू यस इट वाज सो व्हेन वी स्टार्टेड डीबगिंग वी रिलाइज दैट देर वर
डीएनएस फेलर्स दैट र हैपनिंग फॉर दैट पर्टिकुलर आईएसपी एंड दिस वाज अ कंपेरटिवली स्मॉलर आईएसपी च वाज नॉट
रिफ्रेशिंग इट्स डीएनएस और एंट्रीज ऑफ फ्लशिंग इट्स डीएनएस एंट्रीज एंड ट्स व ओनली जिओ सिनेमा वास नॉट ओपनिंग अ कपल ऑफ
आवर डोमेन र फेलिंग विथ डीएनएस फेलर राइट एंड द वे वी ट्रा दैट वी टोल्ड आ कॉली कैन
यू स्विच योर डीएनएस टू 8.8.8 चच इ योर ग डीएनएस राइट एंड द ओपन एंड द स्ट्रीमिंग
वर्क सो देन वी बिल्ट मिटिगेशंस फॉर इट बाय कोडिंग इट इन आवर क्लाइंट एबस दैट हे
इफ यूर गेटिंग अ डीएनएस फेलर यू गो टू अल्टरनेट डीएनएस रिजॉल्वर्स एंड देन यू गो
अहेड एंड ओपन द पप व्हेन योर डीएनएस रेजोल्यूशन आर डन सो इवन दो फॉर कस्टमर
इट्स लाइक जिओ सिनेमा पप इज नॉट ओपनिंग एंड फॉर सीडीएन इट्स लाइक हे यू नो आई गट
द रिक्वेस्ट आई रिटर्न द रिस्पांस फॉर व्हाट एवर रिक्वेस्ट आई एम गेटिंग द फेलियर रेट इज वेरी वेरी लेस बट इट्स
स्टिल इट्स स्टिल आउटसाइड ऑफ योर सिस्टम एंड योर बैक एंड एन योर डीबी दे स्टिल प्रॉब्लम्स लाइक दिस दैट वी गेट टू सी एंड
दिस दिस वन वी एक्चुअली र लाइक एवरी डे इन आईपीएल वी गेट टू सी डिफरेंट सॉर्ट ऑफ
प्रॉब्लम स्टेटमेंट्स दैट कम अप बिकॉज एट स्केल एवरीथिंग इज लाइक अ डिफरेंट बॉल ग
जस्ट एस अ क्यूरियस इंजीनियर हाउ ड यू ड ऑन द फ्लाई बिकॉज आई नो आई कैन चेंज इट इन माय डिवाइस बट फ्रॉम योर एसडी के डू यू डू
यू चेंज योर डीएनएस रिजॉल्वर यस वी डू ट्स हाउ वी मिटिगेटेड इट आई मीन शर वी रीच आउट
टू दोज आईएसपी एंड वी र लाइक हे कैन यू फ्लश योर डीएनएस एंड रिफ्रेश इट बट देर ओनली सो मच यू कैन डू देर आर सो मेनी
आईएसपी राइट इन द कंट्री हु डू यू रीच आउट टू सो वी हैड टू बिल्ड मिटिगेशन ऑन आवर
साइड टू मेक शर द वीडियो प्लेस आई गट वन वेरी इंटरेस्टिंग क्वेश्चन अबाउट हाउ एड्स
वर्क लाइक यू सेड दैट एड्स इज योर क्रिटिकल पाथ लाइक योर मैथ स्ट्रीम शुड वर्क एंड योर एड शुड वर्क सो इफ यू कैन
शेयर अ ब्रीफ डिटेल अबाउट हाउ योर एड्स लाइक स्पेशली न एड्स इंजेक्शन हाउ डू यू
डिसाइड ऑन लॉन्ग वर्सस शॉर्ट एड्स फॉर एग्जांपल द मैच इज ऑन एंड यू हैव टू डिसाइड ट दिस इज द ट आई वुड वांट टू शो
व्हाट्स द फ्लो देर या दिस अ रियली नाइस क्वेश्चन एंड आई थिंक वी वड नीड एन एंटा डिफरेंट पॉडकास्ट टू डिस्कस हाउ एड्स वर्क
एट स्केल इन जयो सिनेमा बट इफ आई एम टू सराइज इट एट अ हाई लेवल देर आर मल्टीपल
वेज इन विच यू कैन डू एड इनसो राइट ओके लेट मी टेक अ स्टेप बैक हाउ हाउ डज एड इन
सशन वर्क सो यू हैव द स्ट्रीम्स कमिंग फ्रॉम योर स्टेडियम राइट एंड वी डू इट इन
मल्टीपल लैंग्वेजेस सो ईच लैंग्वेज हैज इट्स ओन कॉमेंट्री गोइंग ऑन इन दैट लैंग्वेज एंड देर फॉर द स्ट्रीम इज
डिफरेंट नाउ व्हेन द स्ट्रीम्स कम टू अस वी हैव अ प्लेआउट सिस्टम वेयर अ ह्यूमन
ऑपरेटर इज सिटिंग एंड इज लिसनिंग टू द डायरेक्टर ईच स्ट्रीम हैज इट्स ओन डायरेक्टर लाइक यू हैव अ मूवी डायरेक्टर
सो ईच स्ट्रीम हैज अ डायरेक्टर एंड व्हेन द डायरेक्टर सेज गो टू एड्स दैट इज द क्यू
फॉर दैट ऑपरेटर टू अंडरस्टैंड दैट ओके इन माय स्ट्रीम न देर जज नथिंग इंटरेस्टिंग
हैपनिंग और बिटवीन एंड ओवर न देयर इज अ गैप और देर इ स्ट्रेटेजिक टाइम आउट दिस इज
माय चांस टू शो एडस राइट सो दैट पर्सन देन ट्रिगर्स द
एंटायस बीइंग इंसर्टेड और वी विल टॉक अबाउट द डिफरेंट वेज वी कैन डू इट राइट
फर्स्ट थिंग इज स्टैटिक ड इंशन राइट स्टैटिक ड इंशन इ बेसिकली अ ह्यूमन ऑपरेटर ही ही और शी हैज लाइक अ बंच ऑफ एड्स एंड
दे से ओके शो दिस एड टू एवरी एंड
दैट्ची वेर ईच पर्सन गेट्स डिफरेंट ड ट्स वेरी वेरी डिफिकल्ट टू डू एट स्केल वन यू
आर डूइंग वन पर पर्सन बिकॉज यू हैव सच अ शॉर्ट टाइम टू डिसाइड एंड डिलीवर द ड दैट
इट इट्स एन एक्सट्रीमली डिफरेंट डिफिकल्ट प्रॉब्लम स्टेटमेंट द थर्ड टाइप ऑफ एड इंस
यू कैन डू इज क्लाइंट साइड वेर यू सिग्नल योर क्लाइंट वाया स्कट मार्कर्स एंड यू से दैट हे यू कैन स्टार्ट एड द क्लाइंट मेक्स
अ कॉल टू द एड सर्वर एंड देन गेट्स द एड एंड शोज दैट बट देर लॉट ऑफ प्रॉब्लम्स इन
दैट एज वेल बिकॉज योर एबीआर शिफ्ट्स अ लॉट योर सो दैट दैट आल्सो डिफिकल्ट एंड देन
देर द फोर्थ टाइप व्हिच वी डू व्हिच इज कॉल्ड सर्वर साइड एड इंसर्ट सो वी इंसर्ट
एड्स फ्रॉम द बैक एंड बट हाउ वी डू इज वी डू अ लिटिल बिट ऑफ पर्सनलाइजेशन बिकॉज वी
वांट टू डू टारगेटिंग राइट एडवरटाइजर्स वन टारगेटिंग सो वी क्रिएट कोहोर्ट ऑफ पीपल
एंड देन वी टारगेट एड्स ऑन ई कोहो एंड दैट कोहोर्ट कुड बी एनीथिंग इट कुड बी जियोग्राफी इट कुड
बी एंटरटेनमेंट व्यूवर्स क्रिकेट व्यूअर एनीथिंग लाइक दैट इट डिपेंड्स फ्रॉम एडवरटाइजर एंड सिस्टम टू सिस्टम सो या ऑन
हाई लेवल दिस इज हाउ एड्स वर्क वी डू सवर साइड एडन सोशन एंड दैट है बीन वर्किंग गुड
फॉर अस वी डिस्कस अ लट ऑफ थिंग्स एंड आई एम शर लाक ल द इंजीनियर्स ल इंजीनियर्स आर
क्यूरियस बाय नेचर इन एनी वे बट दे र ल फेसिनेटेड बाय हाउ इ एबल टू स्केल टू दिस
अमेजिंग लेवल एंड द इंजीनियरिंग दैट गोज बिहाइंड द आई एम शर यू फोक्स आर हायरिंग डू यू हैव एनी ओपन रोल्स एट द मोमेंट दैट
फोक्स कैन अप्लाई यू आर ऑलवेज हायरिंग ना वी आर ऑलवेज हायरिंग वी आर ऑलवेज हायरिंग
अक्रॉस ऑल ऑफ द वर्टिकल्स एंड आई थिंक द इंटरेस्टिंग पार्ट इज दैट
फॉर अस नो आईपीएल यर इ सेम एंड नो गेम इज सेम दे एवरी एवरी डे दैट वी आर गेटिंग टू
सी अ न्यू सेट ऑफ प्रॉब्लम स्टेटमेंट्स एंड देर नो वन सलूशन फिट्स ल सो वी डू नीड
अ लॉट ऑफ हैंड्स एंड लट ऑफ अमेजिंग डेवलपर्स दैट वी कैन गेट वी आर
कंटीन्यूअसली हायरिंग अक्रॉस ल ऑफ द वर्टिकल्स सो या ल द फोक्स इंटरेस्टेड डू
अप्लाई फॉर व्ट एवर वर्टिकल यू आर इंटरेस्टेड आईल पोस्ट द लिंक इन द डिस्क्रिप्शन डोंट वरी अबाउट इट डट आल डू
दैट बिकॉज लाक इट्स ड्रीम फॉर एवरी इंजीनियर टू वर्क एंड अ कंपनी दैट डज लाइव स्ट्रीमिंग एट दिस यू लर्न सो मच लाइक इवन
इन दिस शॉर्ट डिस्कशन दैट वी हैड यू स्पोक लाइक सच वाइट ब्रेथ ऑफ टॉपिक्स इट्स अ
ड्रीम फॉर एवरी इंजीनियर टू नो ऑल ऑफ दिस अमेजिंग थैंक्स थैंक्स सो मच प्राची फॉर डूइंग दिस इट वास रियली फैब हैविंग यू एंड
यू स्पिल्ड सीक्रेट सम ऑफ देम एंड आई एम शर पीपल वुड लव इट स थैंक्स थैंक सो मच फॉर डूइंग दिस सो मच फॉर हैविंग
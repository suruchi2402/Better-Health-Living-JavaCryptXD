function getBotResponse(input) {

    //rock paper scissors
    if (input == "Doctors") {
        let text="link";
        let sec="Click the following link for getting a list of doctors";
        let res=text.link("https://www.webmd.com/mental-health/doctors-treat-illness");
        return sec+" "+res;
    } else if (input == "Chat") {
        let text1="click here.";
        let sec1="For meeting likeminded people ";
        let sec2="Use Code: 1234";
        let res1=text1.link("https://chatwithfriendsds.herokuapp.com/");
        return sec1+" "+res1+" "+sec2;
    } else if (input == "Recreation") {
        let text2="click here.";
        let sec3="Feeling stressed? Here are some tourist sites for you to see ";
        let res2=text2.link("https://touristercg.herokuapp.com/");
        return sec3+" "+res2;
    }
    else if (input == "Tracker") {
        let text3="click here.";
        let sec4="Wanna keep a track of your mood? ";
        let res3=text3.link("https://moodtracker.link/");
        return sec4+" "+res3;
    }

    // Simple responses
    if (input == "hello") {
        return "Hello there!";
    } else if (input == "goodbye") {
        return "Talk to you later!";
    } else {
        return "Try asking something else!";
    }
}
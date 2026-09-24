const form =
    document.getElementById("predictionForm");


const result =
    document.getElementById("result");


form.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();


        // ====================================
        // GET VALUES FROM FORM
        // ====================================

        const area =
            Number(
                document.getElementById("area").value
            );


        const bedrooms =
            Number(
                document.getElementById("bedrooms").value
            );


        const bathrooms =
            Number(
                document.getElementById("bathrooms").value
            );


        const stories =
            Number(
                document.getElementById("stories").value
            );


        const parking =
            Number(
                document.getElementById("parking").value
            );


        // ====================================
        // CREATE JSON DATA
        // ====================================

        const houseData = {

            area: area,

            bedrooms: bedrooms,

            bathrooms: bathrooms,

            stories: stories,

            parking: parking
        };


        try {

            result.innerHTML =
                "Predicting price...";


            // ====================================
            // SEND DATA TO FASTAPI
            // ====================================

            const response = await fetch("https://house-price-prediction-api-kwtj.onrender.com/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                        },
                body: JSON.stringify(houseData)
            });


            // ====================================
            // RECEIVE RESPONSE
            // ====================================

            const data =
                await response.json();


            // ====================================
            // DISPLAY RESULT
            // ====================================

            const price =
                data.predicted_price;


            result.innerHTML =
                `Predicted Price: ₹${price.toLocaleString("en-IN")}`;


        }

        catch (error) {

            console.error(error);

            result.innerHTML =
                "Unable to connect to backend.";

        }

    }
);
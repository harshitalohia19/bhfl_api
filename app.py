from flask import Flask, request, jsonify

app = Flask(__name__)

FULL_NAME = "harshita_loha"  
DOB = "19072004"        
EMAIL = "harshitalohia@gmail.com"  
ROLL_NUMBER = "22BRS1084"

@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        data = request.json.get("data", [])

        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        alpha_concat = ""
        total_sum = 0

        for item in data:
            if item.isdigit():
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
                total_sum += num
            elif item.isalpha():
                alphabets.append(item.upper())
                alpha_concat += item  # keep original form for concat string
            else:
                special_characters.append(item)

        # concat, reverse, alternating caps
        reversed_alpha = alpha_concat[::-1]
        concat_string = "".join(
            ch.upper() if i % 2 == 0 else ch.lower()
            for i, ch in enumerate(reversed_alpha)
        )

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)

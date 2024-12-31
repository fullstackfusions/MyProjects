## How API Key works for any API providing service:

API keys are unique identifiers used to authenticate and authorize access to APIs (Application Programming Interfaces). They are similar to a password and are used to ensure that only authorized users can make requests to the API.

Here's a high-level overview of how API keys work:

1. **Request an API Key**: When you sign up for an API service, you are typically provided with an API key.
2. **Include the API Key in Requests**: You include this key in the headers or parameters of your API requests.
3. **Authentication**: The server checks the provided API key against its records.
4. **Authorization**: If the key is valid, the server processes the request; if not, it denies access.

### Example: Using `resend` in a Contact Form

Suppose you have a portfolio website with a contact form. When a user submits their email and message, you want to send this information to your email using the `resend` service. Below is an example of how you might set this up using Node.js and the `resend` npm package.

#### Step-by-Step Implementation

1. **Install the `resend` Package**:

   ```bash
   npm install resend
   ```

2. **Set Up Your Environment**:
   Ensure you have your API key from `resend`. This key should be kept secret and not exposed in your frontend code. Use environment variables to store it securely.

   ```bash
   export RESEND_API_KEY="your_resend_api_key"
   ```

3. **Create a Server File (e.g., `server.js`)**:

   ```javascript
   const express = require("express");
   const bodyParser = require("body-parser");
   const resend = require("resend");

   const app = express();
   const port = 3000;

   // Middleware
   app.use(bodyParser.urlencoded({ extended: true }));
   app.use(bodyParser.json());

   // Endpoint to handle form submission
   app.post("/contact", async (req, res) => {
     const { email, message } = req.body;

     try {
       const response = await resend.sendEmail({
         to: "your-email@example.com", // Your email
         from: email, // Sender's email
         subject: "New Contact Form Submission",
         text: message,
       });

       res.status(200).send("Email sent successfully");
     } catch (error) {
       console.error("Error sending email:", error);
       res.status(500).send("Failed to send email");
     }
   });

   app.listen(port, () => {
     console.log(`Server running at http://localhost:${port}`);
   });
   ```

4. **Client-Side Form Submission (e.g., `index.html`)**:

   ```html
   <form id="contactForm">
     <input type="email" name="email" placeholder="Your Email" required />
     <textarea name="message" placeholder="Your Message" required></textarea>
     <button type="submit">Send</button>
   </form>

   <script>
     document
       .getElementById("contactForm")
       .addEventListener("submit", async function (e) {
         e.preventDefault();

         const formData = new FormData(this);
         const data = {
           email: formData.get("email"),
           message: formData.get("message"),
         };

         try {
           const response = await fetch("/contact", {
             method: "POST",
             headers: {
               "Content-Type": "application/json",
             },
             body: JSON.stringify(data),
           });

           if (response.ok) {
             alert("Message sent successfully");
           } else {
             alert("Failed to send message");
           }
         } catch (error) {
           console.error("Error:", error);
           alert("Failed to send message");
         }
       });
   </script>
   ```

#### Explanation:

1. **Express Server**: Set up an Express server to handle form submissions.
2. **Body Parser**: Middleware to parse incoming request bodies.
3. **`/contact` Endpoint**: An endpoint to handle POST requests from the contact form.
4. **`resend.sendEmail`**: Uses the `resend` package to send an email with the provided details.
5. **Client-Side Script**: Handles form submission, sends data to the server, and provides feedback to the user.

### Security Considerations

- **Environment Variables**: Store API keys securely in environment variables.
- **Server-Side Processing**: Keep API keys and sensitive logic on the server side to prevent exposure.

This example should help you understand the basics of using an API key with a service like `resend` to handle contact form submissions.

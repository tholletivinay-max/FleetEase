

async function bookVehicle(vehicleName) {

    const customerName = prompt("Enter your full name:");

    if (!customerName || !customerName.trim()) {
        alert("Please enter your name.");
        return;
    }

    const phone = prompt("Enter your 10-digit mobile number:");

    if (!phone) {
        alert("Phone number is required.");
        return;
    }

    const bookingDate = prompt(
        "Enter your booking date (YYYY-MM-DD):"
    );

    if (!bookingDate) {
        alert("Booking date is required.");
        return;
    }

    try {

        const response = await fetch("/api/bookings", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                vehicle_name: vehicleName,
                customer_name: customerName.trim(),
                phone: phone.trim(),
                booking_date: bookingDate.trim()
            })
        });

        const result = await response.json();

        if (response.ok) {
            alert(result.message);
        } else {
            alert("Booking failed: " + result.message);
        }

    } catch (error) {

        alert("Unable to connect to the server.");

        console.error(error);
    }
}

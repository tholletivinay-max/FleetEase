
async function bookVehicle(vehicleName) {
    const customerName = prompt("Enter your full name:");

    if (!customerName || !customerName.trim()) {
        alert("Please enter your name.");
        return;
    }

    const phone = prompt("Enter your 10-digit mobile number:");

    if (!phone || !/^\d{10}$/.test(phone.trim())) {
        alert("Please enter a valid 10-digit phone number.");
        return;
    }

    const bookingDate = prompt("Enter pickup date (YYYY-MM-DD):");

    if (!bookingDate) {
        alert("Pickup date is required.");
        return;
    }

    const returnDate = prompt("Enter return date (YYYY-MM-DD):");

    if (!returnDate) {
        alert("Return date is required.");
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
                booking_date: bookingDate.trim(),
                return_date: returnDate.trim()
            })
        });

        const result = await response.json();

        if (response.ok) {
            alert(
                result.message +
                "\nRental days: " + result.total_days +
                "\nTotal price: ₹" + result.total_price
            );
        } else {
            alert("Booking failed: " + result.message);
        }

    } catch (error) {
        console.error(error);
        alert("Unable to connect to the server.");
    }
}

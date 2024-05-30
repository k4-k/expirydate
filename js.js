function calculateExpiryDate() {
    var productionDate = document.getElementById('productionDate').value;
    var shelfLife = document.getElementById('shelfLife').value;

    // Convert input to Date object and add shelf life
    var expiryDate = new Date(productionDate);
    expiryDate.setMonth(expiryDate.getMonth() + shelfLife);

    document.getElementById('result').innerHTML = 'Expiry Date: ' + expiryDate.toISOString().split('T')[0];
}
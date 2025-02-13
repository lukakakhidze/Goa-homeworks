<!DOCTYPE html>
<html lang="ka">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>წყალი და ჰაერი - სავიზიტო ბარათები</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="card">
        <h2>💧 წყალი</h2>
        <p><strong>სახელი:</strong> წყალი</p>
        <p><strong>აგრეგატული მდგომარეობა:</strong> თხევადი</p>
        <p><strong>მდებარეობა:</strong> დედამიწის ზედაპირი (ოკეანეები, მდინარეები)</p>
        <p><strong>მნიშვნელობა:</strong> აუცილებელია ყველა ორგანიზმის სიცოცხლისთვის, ასევე რეგულირებს ტემპერატურას.</p>
        <p><strong>შემადგენლობა:</strong> 2 წყალბადის (H) ატომი, 1 ჟანგბადის (O) ატომი</p>
        <p><strong>ძირითადი დამაბინძურებლები:</strong> ქიმიური, ბიოლოგიური</p>
        <p><strong>დაბინძურებისგან დაცვის გზები:</strong> წყლის წმენდა, ეკოლოგიური განათლება</p>
        <p><strong>სამი საინტერესო ფაქტი:</strong></p>
        <ul>
            <li>დედამიწის 70%-ს წყალი ფარავს</li>
            <li>წყალი მავნე ნივთიერებების ამოიღებს</li>
            <li>წყალს შეუძლია ტემპერატურის რეგულირება</li>
        </ul>
    </div>

    <div class="card">
        <h2>🌬️ ჰაერი</h2>
        <p><strong>სახელი:</strong> ჰაერი</p>
        <p><strong>აგრეგატული მდგომარეობა:</strong> აირი</p>
        <p><strong>მდებარეობა:</strong> დედამიწის ატმოსფეროში</p>
        <p><strong>მნიშვნელობა:</strong> აუცილებელია სუნთქვისთვის და კლიმატის რეგულირებისთვის.</p>
        <p><strong>შემადგენლობა:</strong> 78% აზოტი, 21% ჟანგბადი, სხვა ელემენტები</p>
        <p><strong>ძირითადი დამაბინძურებლები:</strong> ნახშირორჟანგი, აზოტის ოქსიდები</p>
        <p><strong>დაბინძურებისგან დაცვის გზები:</strong> გამწვანება, მწვანე ენერგია</p>
        <p><strong>სამი საინტერესო ფაქტი:</strong></p>
        <ul>
            <li>ჰაერი მნიშვნელოვან როლს თამაშობს კლიმატის ცვლილებაში</li>
            <li>ჰაერის 78%-ია აზოტი</li>
            <li>ჰაერი საშუალებას გვაძლევს სუნთქვა და ფუნქციების შესრულება</li>
        </ul>
    </div>
</body>
</html>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f9;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

.card {
    background-color: white;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 300px;
    padding: 20px;
    margin: 20px;
    text-align: left;
}

h2 {
    text-align: center;
    color: #333;
}

ul {
    list-style-type: disc;
    padding-left: 20px;
}

p {
    color: #555;
    line-height: 1.6;
}

.card p, .card ul {
    margin-bottom: 10px;
}

.card:first-child {
    border-left: 5px solid #00aaff;
}

.card:last-child {
    border-left: 5px solid #66cc66;
}

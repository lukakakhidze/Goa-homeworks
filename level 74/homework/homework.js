//1
// 1. Change Text
document.getElementById('changeTextBtn').addEventListener('click', function () {
    document.getElementById('textPara').textContent = "New text!";
  });
  
  // 2. Background Color Every 2 Seconds
  function getRandomColor() {
    return '#' + Math.floor(Math.random() * 16777215).toString(16);
  }
  setInterval(() => {
    document.body.style.backgroundColor = getRandomColor();
  }, 2000);
  
  // 3. Add Names to a List
  document.getElementById('addNameBtn').addEventListener('click', () => {
    const input = document.getElementById('nameInput');
    const ul = document.getElementById('nameList');
    const li = document.createElement('li');
    li.textContent = input.value;
    ul.appendChild(li);
    input.value = '';
  });
  
  // 4. Digital Clock
  function updateClock() {
    const now = new Date();
    document.getElementById('clock').textContent = now.toLocaleTimeString();
  }
  setInterval(updateClock, 1000);
  updateClock();
  
  // 5. Array of Colors (Cycle)
  const colors = ['red', 'green', 'blue', 'purple', 'orange'];
  let colorIndex = 0;
  document.getElementById('colorBtn').addEventListener('click', () => {
    document.body.style.backgroundColor = colors[colorIndex];
    colorIndex = (colorIndex + 1) % colors.length;
  });
  
  // 6. Dynamic Box Creator
  document.getElementById('createBoxesBtn').addEventListener('click', () => {
    const count = parseInt(document.getElementById('boxCount').value);
    const container = document.getElementById('boxContainer');
    container.innerHTML = '';
    for (let i = 0; i < count; i++) {
      const box = document.createElement('div');
      box.style.width = '50px';
      box.style.height = '50px';
      box.style.margin = '5px';
      box.style.display = 'inline-block';
      box.style.backgroundColor = getRandomColor();
      container.appendChild(box);
    }
  });
  
  // 7. Countdown Timer
  let interval;
  document.getElementById('startTimerBtn').addEventListener('click', () => {
    clearInterval(interval);
    let seconds = parseInt(document.getElementById('secondsInput').value);
    const display = document.getElementById('timerDisplay');
    interval = setInterval(() => {
      if (seconds <= 0) {
        clearInterval(interval);
        display.textContent = "Time's up!";
      } else {
        display.textContent = seconds + ' seconds left';
        seconds--;
      }
    }, 1000);
  });
  
  // 9. Typing Speed Test
  const sentences = [
    "JavaScript is fun to learn.",
    "Practice makes perfect.",
    "Coding improves logical thinking."
  ];
  let startTime, targetSentence;
  
  document.getElementById('startTypingBtn').addEventListener('click', () => {
    targetSentence = sentences[Math.floor(Math.random() * sentences.length)];
    document.getElementById('sentence').textContent = targetSentence;
    document.getElementById('typingArea').value = '';
    document.getElementById('typingArea').disabled = false;
    document.getElementById('typingArea').focus();
    startTime = new Date();
  });
  
  document.getElementById('typingArea').addEventListener('input', () => {
    if (document.getElementById('typingArea').value === targetSentence) {
      const endTime = new Date();
      const timeTaken = (endTime - startTime) / 1000;
      const words = targetSentence.split(' ').length;
      const wpm = Math.round((words / timeTaken) * 60);
      document.getElementById('result').textContent = `Time: ${timeTaken.toFixed(2)}s | WPM: ${wpm}`;
      document.getElementById('typingArea').disabled = true;
    }
  });
  
  // 10. Image Slider
  const images = [
    "https://via.placeholder.com/300x200?text=Image+1",
    "https://via.placeholder.com/300x200?text=Image+2",
    "https://via.placeholder.com/300x200?text=Image+3"
  ];
  let currentIndex = 0;
  const imgEl = document.getElementById('sliderImage');
  
  function updateImage() {
    imgEl.src = images[currentIndex];
  }
  
  document.getElementById('prevBtn').addEventListener('click', () => {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    updateImage();
  });
  
  document.getElementById('nextBtn').addEventListener('click', () => {
    currentIndex = (currentIndex + 1) % images.length;
    updateImage();
  });
  
  setInterval(() => {
    currentIndex = (currentIndex + 1) % images.length;
    updateImage();
  }, 3000);
  
  updateImage();
  
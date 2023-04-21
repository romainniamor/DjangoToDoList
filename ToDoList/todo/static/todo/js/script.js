


const animatedTexts = document.querySelectorAll(".animated-text");

  function animateText(animatedText) {
    const text = animatedText.textContent;
    let speed = animatedText.getAttribute("speed");
    let delay = animatedText.getAttribute("delay");
    if (speed == null) {
      speed == 150;
    }
    if (delay == null) {
      delay = 0;
    }
    animatedText.innerHTML = "";
    for (let i = 0; i < text.length; i++) {
      if (text[i] == " ") {
        animatedText.innerHTML += "  ";
      }
      const letterSpan = document.createElement("span");
      letterSpan.textContent = text[i];
      animatedText.appendChild(letterSpan);
    }

    setTimeout(function () {
      let idx = 0;

      function writeChar() {
        const span = animatedText.querySelectorAll("span")[idx];
        span.classList.add("fade");
        idx++;
        if (idx == text.length) {

          clearInterval(writeCharInterval);
        }
      }

      let writeCharInterval = setInterval(writeChar, speed);
    }, delay);
  }

animatedTexts.forEach(animateText);



    document.addEventListener('DOMContentLoaded', function() {
  const starIcon = document.querySelector('.fas.fa-star');
  const priorityCheckbox = document.querySelector('.priorityCheckbox');

  // Vérifiez si la case à cocher est cochée au chargement de la page
  if (priorityCheckbox.checked) {
    starIcon.classList.add('checked');
  }

  priorityCheckbox.addEventListener('click', function() {
    if (priorityCheckbox.checked) {
      starIcon.classList.add('checked');
    } else {
      starIcon.classList.remove('checked');

    }
  });

  const completeCheckbox = document.querySelector('.completeCheckbox');
  const completeBtn = document.querySelector('.done');
  // Vérifiez si la case à cocher est cochée au chargement de la page
  if (completeCheckbox.checked) {
    completeBtn.classList.add('checked');
  }

   completeCheckbox.addEventListener('click', function() {
   console.log("click de complete checkbox")
    if (completeCheckbox.checked) {
      completeBtn.classList.add('checked');
    } else {
      completeBtn.classList.remove('checked');

    }
  });


});




















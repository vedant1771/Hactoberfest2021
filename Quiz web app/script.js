const quizDB= [
    {
        question:"Q1 : What is the full form of HTML?",
        a:"Hello To My Land",
        b:"Hey Text Markup Language",
        c:"HyperText Makeup Language",
        d:"Hyper Text Markup Language",
        ans :"ans4"
    },

    {
        question:"Q2 : Who is making the Web standards??",
        a:"The World Wide Web Consortium",
        b:"Microsoft",
        c:"Google",
        d:"Mozilla",
        ans:"ans1"
    },
    {
        question:"Q3 : Which of these is not absent in HTML? ",
        a:"Tags",
        b:"Source Files",
        c:"Tracking Systems",
        d:"Fat Links",
        ans:"ans1"
    },
    {
        question:"Q4 : Which of these does not support the earlier release of HTML? ",
        a:"Opera",
        b:"Chrome",
        c:"Safari",
        d:"Edge",
        ans:"ans3"
    },
    {
        question:"Q5 : Which of these versions of HTML 4 is called Loose?",
        a:"Frameset",
        b:"Transitional",
        c:"Parser",
        d:"Strict",
        ans:"ans1"
    }
]

const question = document.querySelector('.question');
const option1 = document.querySelector('#option1');
const option2 = document.querySelector('#option2');
const option3 = document.querySelector('#option3');
const option4 = document.querySelector('#option4');
const submit = document.querySelector('#submit');

const answers = document.querySelectorAll('.answer');

const showScore = document.querySelector('#showScore');

let questionCount=0;
let score=0;

const loadQuestion = () => {

    const questionList = quizDB[questionCount];
    question.innerText = questionList.question;

    option1.innerText=questionList.a;
    option2.innerText=questionList.b;
    option3.innerText=questionList.c;
    option4.innerText=questionList.d;
}

loadQuestion();

const getCheckAnswer = () =>{
    let answer;
    answers.forEach(curAnsElem => {
        if(curAnsElem.checked)
        {
        answer=curAnsElem.id;
        }
    });
    return answer;
};

const deselectAll=()=>{
    answers.forEach((curAnsElem)=> curAnsElem.checked = false);
}

submit.addEventListener('click',()=>{
    const checkedAnswer= getCheckAnswer();
    console.log(checkedAnswer);

    if(checkedAnswer === quizDB[questionCount].ans)
    score++;

    questionCount++;

    deselectAll();

    if(questionCount < quizDB.length)
    {
        loadQuestion();
    }else{
        showScore.innerHTML = `
         <h3> You Scored ${score}/${quizDB.length} 🔥</h3>
         <button class = "btn" onclick="location.reload()">Play Again</button>
        `;

        showScore.classList.remove('scoreArea');
    }
});
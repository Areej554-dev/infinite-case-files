document.querySelectorAll(".suspect").forEach(button=>{
  button.addEventListener("click",()=>{
    const chosen=button.dataset.name;
    const result=document.querySelector("#result");
    const title=document.querySelector("#result-title");
    const text=document.querySelector("#result-text");
    document.querySelectorAll(".suspect").forEach(b=>b.disabled=true);
    result.classList.remove("hidden");
    if(chosen===culprit){
      document.querySelector("#result-icon").textContent="✓";
      title.textContent="CASE SOLVED";
      text.textContent=`${chosen}'s statement was the one that conflicted with the independent record.`;
    }else{
      document.querySelector("#result-icon").textContent="×";
      title.textContent="WRONG ACCUSATION";
      text.textContent=`${chosen} was not the culprit. Compare every statement with its matching record.`;
    }
  });
});

let editor = CodeMirror.fromTextArea(document.getElementById("code"), {
    lineNumbers: true,
    mode: "python",
    theme: "default"
});

document.getElementById("language").addEventListener("change", function () {
    const lang = this.value;
    if (lang === "python") editor.setOption("mode", "python");
    else editor.setOption("mode", "text/x-java"); 
});

document.getElementById("runBtn").addEventListener("click", function () {
    const language = document.getElementById("language").value;
    const code = editor.getValue();

    fetch("/run", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `language=${language}&code=${encodeURIComponent(code)}`
    })
    .then(res => res.text())
    .then(data => {
        document.getElementById("output").textContent = data;
    });
});

document.getElementById("saveBtn").addEventListener("click", () => {
    const lang = document.getElementById("language").value;
    const code = editor.getValue();
    localStorage.setItem("saved_" + lang, code);
    alert("Code saved!");
});

document.getElementById("loadBtn").addEventListener("click", () => {
    const lang = document.getElementById("language").value;
    const code = localStorage.getItem("saved_" + lang);
    if (code) {
        editor.setValue(code);
    } else {
        alert("No saved code found for " + lang);
    }
});

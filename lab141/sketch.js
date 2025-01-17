let ender;

function preload(){
    ender = loadModel("ender3v3_model.stl", true);
}

function setup(){
    createCanvas(window.innerWidth, window.innerHeight, WEBGL);
}

function draw(){
    //camera (0, 1000, 200);
    colorMode (RGB);
    background(214, 63, 63);
    scale (width * 0.0014);
    orbitControl(1, 1, 0);
    noStroke();
    directionalLight (0, 0, 840, 0.5, 0.5, -0.5);
    specularMaterial (250);
    shininess (1);
    model(ender);
}
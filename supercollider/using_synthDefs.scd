// producing a synthDef
// A synthDef is basically a recipe for a sound
// And a 'synth' is the execution of that recipe


// store synth function in x
(x = { SinOsc.ar(exprand(400, 750)) }.play;)


// to free the synth up (stop it from producing sound)
x.free;




y = { SinOsc.ar(800, SinOsc.ar(XLine.kr(1, 1000, 9), 0, 2pi), 0.25) };

y = y.play;


y.free;

















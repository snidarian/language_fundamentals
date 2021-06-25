// =====================================================================
// SuperCollider Workspace
// =====================================================================


// basic
//x = { SinOsc.ar(700) }.play

//x;

//x.free;


// same thing but with changable arguements that can be set and changed at runtime

/*
(
z = {arg freq=350, amp=1;var sig;sig = SinOsc.ar(freq) * amp;}.play;
)

z.set(\freq, 450)
z.set(\freq, 520)
z.set(\freq, 690)
z.free;
*/

(
z = {
	arg noiseHz=8;
	var freq, sig;
	freq = LFNoise0.kr(noiseHz).exprange(80, 1200);
	sig = SinOsc.ar(freq);
}.play;
)


// You can evaluate this while the above function is running to change the speed of random notes
z.set(\noiseHz, 2);

// use 'exprand(min, max)' to generate random values like with random.randint in python3
z.set(\noiseHz, exprand(1, 40));





z.free;

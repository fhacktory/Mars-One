#pragma strict

import UnityEngine.Networking;

var previousMessage: MessageImage;
var webcamComponent: Webcam;

var lastSentAt:float = -1f;
var freq:float = 2f;
var start: int;

var multiplier: int = 8;
var currentStep: int = 0;

public class MessageImage extends UnityEngine.Networking.MessageBase {
	public var messageValue: byte[];
	public var width: int;
	public var height: int;
	public var step: int;
}

public class MessagePixel extends UnityEngine.Networking.MessageBase {
	public var colors: Color32[];
	public var start: int;
	public var end: int;
	public var width: int;
	public var height: int;
}


function send(message: MessageImage) {

	NetworkServer.SendToAll(MsgType.Highest + 1, message);
	//NetworkServer.SendByChannelToAll(MsgType.Highest + 1, message);
}

function Start () {
	NetworkServer.Listen(4444);

	webcamComponent = this.GetComponent.<Webcam>();

	start = 0;
}

function Update () {

/*

    send(message);*/

	//var cols:Color32[] = webcamComponent.webcamTexture.GetPixels32();

	var maxSteps: int = multiplier;

	if(currentStep >= maxSteps) {
		currentStep = 0;
	}

	Debug.Log('maxSteps ' + maxSteps + ' currentStep ' + currentStep);

	var imageWidth: int = webcamComponent.webcamTexture.width;
	var imageHeight: int = webcamComponent.webcamTexture.height;

	var stepWidth: int = imageWidth / multiplier;
	var stepHeight: int = imageHeight / multiplier;

	var txt: Texture2D = new Texture2D(stepWidth, stepHeight);
	var total: Color32[] = webcamComponent.webcamTexture.GetPixels32();

	var subTotalSize: int = total.Length / (multiplier * multiplier);

	var subTotal: Color32[] = new Color32[subTotalSize];

	var k: int = 0;

	var x: int = currentStep * stepWidth;
	var y: int = currentStep * stepHeight;

	//Debug.Log('currentStep ' + currentStep + ' x ' + x + ' y ' + y);

	var blank:int = x + stepWidth + imageWidth - stepWidth;

	for(var i: int = y; i < y + stepHeight; i++) {
		for(var j:int = x; j < x + stepWidth; j++) {
			subTotal[k] = total[i * imageWidth + j];
			k++;
		}
	}

    txt.SetPixels32(subTotal);

    var message: MessageImage = new MessageImage();
    message.messageValue = txt.EncodeToJPG(75);
    message.step = currentStep;
    message.width = imageWidth / multiplier;
    message.height = imageHeight / multiplier;

    currentStep++;

    send(message);

	//var cols: byte[] = txt.EncodeToJPG(75);


    /*if(start >= cols.Length) {
    	start = 0;
    }


    var end: int = start + (imageWidth * imageHeight / 2700);

    if(end >= cols.Length) {
    	end = cols.Length;
    }

    var colors:Color32[] = new Color32[end - start];

    for(var i: int = start; i < end; i++) {
        colors[i - start] = cols[i];
    }

    var p: MessagePixel = new MessagePixel();
    p.colors = colors;
    p.start = start;
    p.end = end;
    p.width = imageWidth;
    p.height = imageHeight;

    NetworkServer.SendToAll (MsgType.Highest + 2, p);

    start = end;*/







	/*for(var i:int = 0; i < webcamComponent.data.Length;i++) {
		var message: MessagePixel = new MessagePixel();
		message.color = webcamComponent.data[i];
		message.index = i;
		NetworkServer.SendToAll(MsgType.Highest + 2, message);
	}*/

	/*
	var message: MessageImage = new MessageImage();

	//message.messageValue = webcamComponent.data;
	message.messageValue = new Color32[1];
	message.messageValue[0] = new Color32();

	send(message);
	*/
}
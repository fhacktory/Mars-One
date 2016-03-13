#pragma strict
var baseRotation: Quaternion;
var webcamTexture: WebCamTexture;
//var data : Color32[];

var previousWidth : int;
var previousHeight : int;

function Start () {

	webcamTexture = new WebCamTexture();

	var renderer: Renderer = GetComponent.<Renderer>();

	renderer.material.mainTexture = webcamTexture;

	baseRotation = transform.rotation;

	webcamTexture.Play();

	UpdateDataIfNeeded();

}

function UpdateDataIfNeeded () {
	if(webcamTexture.width != previousWidth || webcamTexture.height != previousHeight) {
		//data = new Color32[webcamTexture.width * webcamTexture.height];

		previousWidth = webcamTexture.width;
		previousHeight = webcamTexture.height;
	}

}

function Update () {
	transform.rotation = baseRotation * Quaternion.AngleAxis(webcamTexture.videoRotationAngle, Vector3.up);

	//UpdateDataIfNeeded();
	//webcamTexture.GetPixels32(data);
}
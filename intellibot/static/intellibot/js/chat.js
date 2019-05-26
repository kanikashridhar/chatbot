// START WEBSOCKETS            
var supportsWebSockets = ('WebSocket' in window || 'MozWebSocket' in window) && WebSocket;
if(!supportsWebSockets){
	$(".very-old-browser-notification").show();
	$(".non-error").hide();
}else{
	$(".very-old-browser-notification").hide();
	$(".non-error").show();
}
var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";

// Calls the websocket
var chatsock = new WebSocket(ws_scheme + '://' + window.location.host + "/ws/chat");

$("#messageToSend").keypress(function (e) {
	var key = e.which;                
	if (key == 13)  // trigger message send when 'enter' key is clicked
	{
		$('#messageSendButton').trigger('click');
		return false;
	}
});

// Code that is called when the socket is succesfully opened
chatsock.onopen = function(message) {
	
	$('.error-notification').hide();
	$('.non-error').show();
	$('#messages-container').html('<div  class="empty-div"></div>');
	message = {}
	message.command= 'start';
	console.log('sent message ', JSON.stringify(message));
	chatsock.send(JSON.stringify(message)); // START TALKING!
}
chatsock.onmessage = function(message){
	processAndDisplayChatMessage(message);
};

chatsock.onclose = function(message){
	console.log("connection lost ... ");
}

chatsock.onerror = function(message){
	console.log("Error reconnecting ... ");
	$('.error-notification').html("Unable to connect to the awesome chatbot server. Please try again in a few minutes (by refreshing the page).")
	$('.error-notification').show();
	$('.non-error').hide();
	$("#body-container").scrollTop( $('#body-container')[0].scrollHeight );   
}

$(document).ready(function() {
	$("#body-container").scrollTop( $('#body-container')[0].scrollHeight );
});


// Function to simply format the text in the right way. May end up being more complicated when you have MCQs, etc.
function generate_formatted_chat_message(data){
	if(data.type == 'text'){
		message_text = '<span class="message-text" data-messageId="'+data.id+'" data-context="'+data.context+'">' + data.text + '</span>'
		return message_text;
	}
	console.log("invalid data format");
	return "";
}

// Function that adds a message to the chat window
function add_message_to_chat(data, formatted_div){
	var chat = $('#messages-container');
	var new_source = data["source"];
	if (new_source == "BOT"){
		chat.append('<div class="msg-row"><div class="col-xs-11 col-sm-11 col-md-11 col-lg-11 no-sides-padding msg-animate"><div class="bot-icon-div">Bot:</div><div class="panel message-panel bot-msg "><div class="panel-body bot-msg-body"><div><div class="message-text">'+formatted_div+'</div></div></div></div></div></div>');
	}else if(new_source == "CANDIDATE"){

		var child = $('<div class="msg-row">');
		$(child).append('<div class="row"><div class="col-xs-10 col-sm-10 col-md-10 col-lg-10  pull-right no-sides-padding msg-animate"><div class="panel message-panel user-msg"><div class="panel-body user-msg-body"><div class="message-text"><span></span></div></div></div><div class="user-msg-bubble">you</div></div>');
		$(child).find('span').html(formatted_div);
		chat.append(child);
	}
	$("#body-container").scrollTop( $('#body-container')[0].scrollHeight);	
}  


// Function taht is called when the server sends a message via websockets to my front end.
function processAndDisplayChatMessage(message){
	console.log('recieved message', message);
	var content_data = JSON.parse(message.data);
	var formatted_div = generate_formatted_chat_message(content_data);	
	if(formatted_div.length > 0){
		add_message_to_chat(content_data, formatted_div);
	}
	if(content_data.context == 'DONE'){
		// show Done button and hide message input box
		$("#send-box").hide()
		$("#done-box").removeClass('hidden')
	}
}

function sendTextMessage() {
    if ($('#messageToSend').text() == "") {
        return
    }

    message = {}
    message.text = $('#messageToSend').html().replace("</div>", "").replace("<div>", "\n").replace("<br>", "\n");
    message.command= 'send'
	message.timestamp = new Date();

	// Get the last question asked - send context and id of that question to server with this message
	totalQuestionsSoFar = $('#messages-container span.message-text').length;
	lastQuestion = $('#messages-container span.message-text')[totalQuestionsSoFar-1];
	message.context = $(lastQuestion).data('context');
	message.id = $(lastQuestion).data('messageid');
    
    $('#messageToSend').text('');
	chatsock.send(JSON.stringify(message));
	$("#message").val('').focus();
	console.log('sent message ', JSON.stringify(message));
    return false;   
}

function sendDoneMessage(){
	message = {}
	message.command = 'finish'
	chatsock.send(JSON.stringify(message));
	$("#doneButton").attr("disabled", "disabled");
}
		
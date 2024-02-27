var server_port = 65432;
var server_addr = "192.168.0.191";   // the IP address of your Raspberry PI

function client(command=""){
    
    const net = require('net');
    var input = document.getElementById("myName").value;

    const client = net.createConnection({ port: server_port, host: server_addr }, () => {
        // 'connect' listener.
        console.log('connected to server!');
        // send the message
        if(command != ""){
            client.write(`${command}\r\n`);
        }
        else{
        client.write(`${input}\r\n`);
    }
    });
    
    // get the data from the server
    client.on('data', (data) => {
        d = data.toString().split(":");
        document.getElementById("speed").innerHTML = d[0];
        document.getElementById("direction").innerHTML = d[1];
        document.getElementById("step_array").innerHTML = d[2];
        //document.getElementById("greet_from_server").innerHTML = data;
        console.log(d.toString());
        client.end();
        client.destroy();
    });

    client.on('end', () => {
        console.log('disconnected from server');
    });


}

function greeting(){
    console.log("greeting");
    // get the element from html
    var name = document.getElementById("myName").value;
    // var stop = document.getElementById("top");
    // stop.onclick = function(){
    //     print("stop");
    // }
    // update the content in html
    
    document.getElementById("greet").innerHTML = "Hello " + name + " !";
    //document.getElementById("result").innerHTML = "Waiting for the server to respond...";
    // send the data to the server 
    //to_server(name);
    client();

}
function move(command=""){
    
    client(command);
}

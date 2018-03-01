var a = [];
for(var i = 1;i<=9;i++)
{
 a.push(

function(i){
    $('#image'+i).mouseover(function(){
      
        $('#register'+i).fadeIn(1);

    });

    $('#image'+i).mouseout(function(callback){

      console.log("hi");
      $('#register'+i).fadeOut(1);
      $('#registerinf'+i).fadeOut(1);
    });

}
 )
}

for(var i = 0 ; i<9;i++)
{
a[i](i+1);
}

function register(name){
$('#regformcon'+name).fadeIn(1);
$('#regform'+name).fadeIn(1);

}

function registerc(s){
$('#regformcon'+s).fadeOut(1);
$('#regform'+s).fadeOut(1);
console.log("ji");
}

function info(s)
{
  document.getElementById("registerinf"+s).style.display ="block";
  $('#register'+s).fadeOut(1);
}

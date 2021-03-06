/* Create a cache object */
var cache = new LastFMCache();

/* Create a LastFM object */
var lastfm = new LastFM({
  apiKey    : '552cfc676846a20bd4b95b752050d1b7',
  apiSecret : 'd62db089020881f653dccbfc9a1d4cb9',
  cache     : cache
});

lastfm.user.getInfo({user: 'nicksiz'}, {success: function(info){

  var register =  info.user.registered["#text"];
  register = register.split(" ")[0];

  // console.log(info);
  document.getElementById("recent").innerHTML += '<div class="one columns">' +
    '<img src="'+info.user.image[1]["#text"]+'"/> </div>';

  document.getElementById("recent").innerHTML += '<div class="two columns" style="padding: 5 5px;">' +
    "<a href="+info.user.url+">" +
    "jeffisabelle" + "</a>" + " <br /> " +
    info.user.playcount +" tracks scrobbled <br /> since " +
    register +"<br /><br /></div>";


}});

lastfm.user.getRecentTracks({user: 'nicksiz'}, {success: function(recent){

  // console.log(recent);

  var i = 0;
  var gosterilecek = 3;
  while(i < gosterilecek) {
    if(recent.recenttracks.track[i].image[1]["#text"]) {
      document.getElementById("recent").innerHTML += '<div class="one columns">' +
        '<img src="'+recent.recenttracks.track[i].image[1]["#text"]+'"/> </div>';

      if(i===gosterilecek-1) {
        document.getElementById("recent").innerHTML += '<div class="two columns" style="padding: 5 5px;">' +
          "<a href="+recent.recenttracks.track[i].url+">" +
          recent.recenttracks.track[i].name + "</a>" + " <br /> by " +
          recent.recenttracks.track[i].artist["#text"]+"<br /> at " +
          recent.recenttracks.track[i+1].date["#text"]+"<br /><br /></div>";
      } else {
        document.getElementById("recent").innerHTML += '<div class="two columns" style="padding: 5 5px;">' +
          "<a href="+recent.recenttracks.track[i].url+">" +
          recent.recenttracks.track[i].name + "</a>" + " <br /> by " +
          recent.recenttracks.track[i].artist["#text"]+"<br /> at " +
          recent.recenttracks.track[i+1].date["#text"]+"<br /><br /></div>";
      }

    } else {
      gosterilecek++;
    }

    i++;
  }

}, error: function(code, message){

}});

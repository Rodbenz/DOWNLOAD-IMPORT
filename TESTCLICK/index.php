<html>
    <title>TEST CLICK .BAT</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <head>TEST CLICK .BAT</head>
    <body>
        <div>
            <button type="button" id="btnClick">MANUAL</button>
            <!-- <label for="select12">ประเภทคำขอ:</label> -->
            <!-- <select name="select12" id="select12" class="form-control">
                <option value="0">กรุณาเลือก</option> -->

        </div>
    </body>
    <script>
        // $(document).ready(function(){
        //     var optiontag = "<option value = '0' > -- เลือกช่วงทางพิเศษ -- </option>"
        //         $('#select12').empty().append(optiontag)
        //     var settings = {
        //         "url": "http://192.168.100.83:8090/api/MAS/requestByStatus/N",
        //         "method": "GET",
        //         "timeout": 0,
        //         };

        //         $.ajax(settings).done(function (response) {
        //         console.log(response);
        //         for(var i in response){
        //             var optiontag = "<option value ='" + response[i].REQUEST_ID + "'> " + response[i].REQUEST_NAME_TH + " </option>"
        //                     $('#select12').append(optiontag)
        //         }
        //         });
        // })
        $(document).on('click','#btnClick',function(){
            var settings = {
                "url": "http://localhost:8090/api/common/updateSatatus",
                "method": "POST",
                "timeout": 0,
                "async":false,
                "dataType": "json",
                "headers": {
                    "Content-Type": "application/json"
                },
                "data": JSON.stringify({
                    "status": "N"
                }),
                };

                $.ajax(settings).done(function (response) {
                console.log(response);
                });
        });
    </script>
</html>
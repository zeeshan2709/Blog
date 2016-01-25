angular.module("com_form", []).controller("com_ctrl", function($scope) {
            $scope.myForm = {};
            $scope.myForm.comment=lookup();
            $scope.myForm.submitTheForm = function (){
                com = document.getElementById("comm").value;
                if(com==""){
                    alert("write something biatchh!!");
                } else {
                    document.getElementById("comm").value = "";
                    $.ajax({
                        type: "POST",
                        url: "{% url "comment" %}",
                        data: {'comment':com, 'slug': $(this).attr('slug'), 'csrfmiddlewaretoken': '{{csrf_token }}'},
                        dataType: "json",
                        success:function(){
                            alert("commented!!");
                            $scope.myForm.comment=lookup();
                            $scope.$digest();
                        }
                    });
                }
            };

        } );
        function lookup() {
            var result = [];
            var data = $.parseJSON($.ajax({
                type: "GET",
                url: "{% url "comment" %}",
                data: {'slug': $(this).attr('slug'), 'csrfmiddlewaretoken': '{{ csrf_token }}'},
                dataType: "json",async: false}).responseText);
            result = data;
            console.log(result);
            return result; 
        }
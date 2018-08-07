$(document).ready(function() {
	var newListItem;
	var newList = true;
	var theList = document.getElementById('theList');

	$('#addToDo').on('click', function(e) {
		e.preventDefault();
		if (newList == true) {
			var theValue = $("#toDoItem").val();
			newListItem = '<li><span class="handle"> :: </span> <input class="listItem" value="' + theValue + '"><a class="removeListItem" style="display: none;" href="#"> X </a> </li>';
			newList = false;	
		} else {
			var theValue = $("#toDoItem").val();
		    newListItem = $('#theList li:last').clone();
			newListItem.find('input').attr('value', theValue); 
		}

		var theCount = $("#theList li").length + 1;
		if (theCount > 1) {
			$('#doClearAll').css('display','block');
		}

		$('#theList').append(newListItem);


		$('#toDoItem').val('');
		$('#toDoItem').focus();
		$('.sortable').sortable('destroy');
		$('.sortable').sortable({
			handle: '.handle'
		});

	});
		
});

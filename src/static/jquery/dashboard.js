$(document).ready(function() {
    $('.choose_list p').click(function() {
        $(this).fadeOut();
    });


});


jQuery(function($) {
        $('.selector').delegate('.remove-product', 'click', function() {
            $(this).parent().fadeOut();
            var $this = $(this);
            var product_id = $this.data('product-id');
            $.post(URLS.REMOVE_ITEM,{'product_id':product_id},function(){
                $this.parents('.product-item').remove();
            })
        });

        $('.add-item').on('click',function(){
            var $this = $(this);
            var product_id = $this.data('product-id');
            $.post(URLS.ADD_ITEM,{'product_id':product_id},function(response){
                $(".items_of_buylist").prepend(
                    '<p class="product-item">'+
                    response + ' '+
                    '<i data-product-id="'+
                    product_id +
                    '" class="icon-remove-circle remove-product"></i></p>');
            });
        });


        $('.buy-products').on('click',function(){
            var $this = $(this);
            $.post(URLS.BUY_ITEMS,function(response){

            })
        })
        $('.buy-products').on('click',function(){
                $(".product-item").remove();
        })

    });


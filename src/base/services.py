from django.core.exceptions import ValidationError


def get_new_product_img_path(instance, file) -> str:
    """
    Return custom image path based on product id
    """
    return f"products/product_{instance.product.id}/{file}"


def validate_size_image(file_obj):
    """
    Check an image file size
    """
    megabyte_limit = 2
    if file_obj.size > megabyte_limit * 1024 * 1024:
        raise ValidationError(f"Max image file size {megabyte_limit}MB")

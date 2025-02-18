"""
Definition of the :class:`SeriesSerializer` class.
"""
from django_dicom.models.patient import Patient
from django_dicom.models.series import Series
from django_dicom.models.study import Study
from rest_framework import serializers


class SeriesSerializer(serializers.ModelSerializer):
    """
    A serializer class for the :class:`~django_dicom.models.series.Series`
    model.
    """

    study = serializers.PrimaryKeyRelatedField(queryset=Study.objects.all())
    patient = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all()
    )

    class Meta:
        model = Series
        fields = (
            "id",
            "study",
            "patient",
            "body_part_examined",
            "patient_position",
            "number",
            "description",
            "date",
            "time",
            "modality",
            "protocol_name",
            "pulse_sequence_name",
            "sequence_name",
            "scanning_sequence",
            "sequence_variant",
            "pixel_spacing",
            "slice_thickness",
            "echo_time",
            "inversion_time",
            "repetition_time",
            "flip_angle",
            "manufacturer",
            "manufacturer_model_name",
            "magnetic_field_strength",
            "device_serial_number",
            "institution_name",
            "uid",
            "sequence_type",
        )

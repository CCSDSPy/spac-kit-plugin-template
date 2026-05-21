"""Metadata packet definition for example instrument.

This packet type typically contains configuration and status information.
"""
import ccsdspy


# Example metadata packet fields
metadata_example_fields = [
    # CCSDS Primary Header
    ccsdspy.PacketField(name="CCSDS_VERSION", bit_length=3, data_type="uint"),
    ccsdspy.PacketField(name="CCSDS_TYPE", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="CCSDS_SEC_HDR_FLG", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="CCSDS_APID", bit_length=11, data_type="uint"),
    ccsdspy.PacketField(name="CCSDS_SEQ_FLGS", bit_length=2, data_type="uint"),
    ccsdspy.PacketField(name="CCSDS_SEQ_CNT", bit_length=14, data_type="uint"),
    ccsdspy.PacketField(name="CCSDS_PKT_LEN", bit_length=16, data_type="uint"),

    # Metadata fields
    ccsdspy.PacketField(name="SOFTWARE_VERSION", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="HARDWARE_VERSION", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="CONFIG_ID", bit_length=32, data_type="uint"),
]

metadata_example = ccsdspy.VariableLength(
    metadata_example_fields,
    name="example_metadata",
    apid=101
)

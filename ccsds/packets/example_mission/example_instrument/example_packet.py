"""Example Health and Status packet structure.

This is a template showing how to define a CCSDS packet structure.
Replace with your actual packet definitions based on your ICD.
"""
import ccsdspy


# Example: Define packet fields based on your Interface Control Document (ICD)
example_health_status_fields = [
    # CCSDS Primary Header fields (typically 48 bits / 6 bytes)
    ccsdspy.PacketField(name="CCSDS_VERSION", bit_length=3, data_type="uint"),
    ccsdspy.PacketField(name="CCSDS_TYPE", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="CCSDS_SEC_HDR_FLG", bit_length=1, data_type="uint"),
    ccsdspy.PacketField(name="CCSDS_APID", bit_length=11, data_type="uint"),
    ccsdspy.PacketField(name="CCSDS_SEQ_FLGS", bit_length=2, data_type="uint"),
    ccsdspy.PacketField(name="CCSDS_SEQ_CNT", bit_length=14, data_type="uint"),
    ccsdspy.PacketField(name="CCSDS_PKT_LEN", bit_length=16, data_type="uint"),

    # Secondary header (example - customize based on your mission)
    ccsdspy.PacketField(name="TIMESTAMP_SECONDS", bit_length=32, data_type="uint"),
    ccsdspy.PacketField(name="TIMESTAMP_SUBSECONDS", bit_length=16, data_type="uint"),

    # Data fields (example - replace with your actual telemetry fields)
    ccsdspy.PacketField(name="INSTRUMENT_TEMP", bit_length=16, data_type="int"),
    ccsdspy.PacketField(name="POWER_VOLTAGE", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="POWER_CURRENT", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="OPERATING_MODE", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="ERROR_FLAGS", bit_length=8, data_type="uint"),
    ccsdspy.PacketField(name="COMMAND_COUNT", bit_length=16, data_type="uint"),
    ccsdspy.PacketField(name="ERROR_COUNT", bit_length=16, data_type="uint"),
]

# Create a VariableLength packet definition
# Use FixedLength if your packets have a fixed size
example_health_status = ccsdspy.VariableLength(
    example_health_status_fields,
    apid=100,
    name="example_health_status"
)

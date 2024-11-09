package P3;

public enum Pay {
    CHARGE_TYPE_CHARGED("10131001","自费"),
    CHARGE_TYPE_FREE("10131002","免费"),
    CHARGE_TYPE_MEMBER_RIGHTS("10131003","会员权益");



    private String code;
    private String isFree;

    Pay(String code, String isFree) {
        this.code = code;
        this.isFree = isFree;
    }

    public String getCode() {
        return code;
    }

    public String getIsFree() {
        return isFree;
    }
}

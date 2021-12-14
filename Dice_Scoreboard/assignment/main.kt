import java.util.Random
/*
 * 주사위와 점수판 두개의 클래스를 작성합니다.
 * 주사위에서는 최대 10의 값을 가지는 정수를 출력하여 점수판에 전달하며, 점수판 클래스는 주사위에서 출력하는 점수를
 * 기록하고 총 20개의 점수를 기록하게 되면 점수들을 출력합니다.
 * 코드에는 get/set 함수가 꼭 포함되어야 합니다.
 * 점수판에는 다음과 같은 규칙을 적용하여 점수를 기록합니다
 * -똑같은 점수가 연속으로 들어오면 받아온 점수에 10점을 추가하여 기록합니다
 * -점수판에서 점수를 출력할 때 15를 넘는 값은 15로 출력합니다
 * (이번주 과제는 기본적인 문법을 익히기 위한 과제이며, 다음주 부터는 코틀린을 안드로이드에서 적용할 예정이니 참고 바랍니다)
 * 이번주 과제 코드는 https://play.kotlinlang.org/ 에서 작성하여 실행 스크린샷, 소스코드를 제출해주세요.
 */
class Dice(){
    var score: Int = 0
    	set(value){
           field = Random().nextInt(value) + 1 //값을 바꾸면 항상 1 ~ 10 범위의 값 저장
        }
        get(){
            return field
        }
}    

class Score_Board(val d: Dice, val num: Int){
    private var last_input: Int = -1
    var log: Array<Int> = Array(20,{0})
    init{
        for(i in 0..19){
            d.score = num
            println(d.score.toString())
            log[i] = d.score
            if (d.score == last_input){
                log[i] += 10
            }
            last_input = d.score
        }
        println("=====================")
    }
    fun show(){
      for(i in 0..19){
            if(log[i] > 15) println("15")
            else println(log[i].toString())
        }
    }
}

fun main() {
    val d = Dice()
    val s = Score_Board(d,10)
    s.show()
}
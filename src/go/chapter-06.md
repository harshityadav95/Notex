# Chapter 6. Writing Tests

## A Note for Early Release Readers

With Early Release ebooks, you get books in their earliest form—the author’s raw and unedited content as they write—so you can take advantage of these technologies long before the official release of these titles.

This will be the fifteenth chapter of the final book. Please note that the GitHub repo will be made active later on.

If you’d like to be actively involved in reviewing and commenting on this draft, please reach out to the editor at sgrey@oreilly.com.

Since the 2000s, the widespread adoption of automated testing has probably done more to improve code quality than any other software engineering technique. As a language and ecosystem focused on improving software quality, it’s not surprising that Go includes testing support as part of its standard library. Go makes it so easy to test your code, there’s no excuse to not do it.

In this chapter, you’ll see how to test Go code, group tests into unit and integration tests, examine code coverage, write benchmarks, and learn how to check code for concurrency issues by using the Go data race detector. Along the way, I’ll discuss how to write code that is testable and why this improves our code quality.

## Understanding the Basics of Testing

Go’s testing support has two parts: libraries and tooling. The testing package in the standard library provides the types and functions to write tests, while the go test tool that’s bundled with Go runs your tests and generates reports. Unlike many other languages, Go places its tests in the same directory and package as the production code. Every test is written in a file whose name ends with _test.go. If you are writing tests against foo.go, place your tests in a file named `foo_test.go`. Since tests are located in the same package, they can access and test unexported functions and variables. You’ll see in a bit how to write tests that ensure that you are testing only a public API.

> **Note**
>
> Complete code samples for this chapter are found in the Chapter 15 repository.

Let’s write a simple function and then a test to make sure the function works. In the `sample_code/adder` directory, in the file adder.go, you have the following:

```go
func addNumbers(x, y int) int {
    return x + x
}
```

The corresponding test is in `adder_test.go`:

```go
func Test_addNumbers(t *testing.T) {
    result := addNumbers(2,3)
    if result != 5 {
        t.Error("incorrect result: expected 5, got", result)
    }
}
```

Test functions start with the word Test and take in a single parameter of type *`testing.T`. By convention, this parameter is named t. Test functions do not return any values. The name of the test (apart from starting with the word “Test”) is meant to document what you are testing, so pick something that explains what you are testing. When writing unit tests for individual functions, the convention is to name the unit test Test followed by the name of the function. When testing unexported functions, some people use an underscore between the word Test and the name of the function.

Also note that you use standard Go code to call the code being tested and to validate that the responses are as expected. When there’s an incorrect result, you report the error with the `t.Error` method, which works like the `fmt.Print` function. You’ll see other error-reporting methods in a bit.

You’ve just seen the library portion of Go’s test support. Now let’s take a look at the tooling. Just as go build builds a binary and go run runs a program, the command go test runs the test functions in the current directory:

```console
$ go test
--- FAIL: Test_addNumbers (0.00s)
    adder_test.go:8: incorrect result: expected 5, got 4
FAIL
exit status 1
FAIL    test_examples/adder     0.006s
```

It looks like you found a bug in your code. Taking a second look at addNumbers, you see that you are adding x to x, not x to y. Let’s change the code and rerun the test to verify that the bug is fixed:

```console
$ go test
PASS
ok      test_examples/adder     0.006s
```

> **Tip**
>
> There are many ways to control the behavior of go test. Some of the most helpful are:

- Pass a file or directory name to go test to run tests in that file or directory. Using ./... runs all tests in the current directory and all subdirectories (go test ./...)

- The -v flag runs tests with verbose output.

- Use the -run flag to provide a test name or pattern to specify which test functions to run. (go test -run=Test_addNumbers)

For a complete listing of go test flags and configuration, run go help testflag.

### Reporting Test Failures

There are several methods on *`testing.T` for reporting test failures. You’ve already seen Error, which builds a failure description string out of a comma-separated list of values.

If you’d rather use a Printf-style formatting string to generate your message, use the Errorf method instead:

```go
t.Errorf("incorrect result: expected %d, got %d", 5, result)
```

While Error and Errorf mark a test as failed, the test function continues running. If you think a test function should stop processing as soon as a failure is found, use the Fatal and Fatalf methods. The Fatal method works like Error, and the Fatalf method works like Errorf. The difference is that the test function exits immediately after the test failure message is generated. Note that Fatal only ends the current test; any remaining test functions will execute after the current test function exits.

When should you use Fatal/Fatalf and when should you use Error/Errorf? If the failure of a check in a test means that further checks in the same test function will always fail or cause the test to panic, use Fatal or Fatalf. If you are testing several independent items (such as validating fields in a struct), then use Error or Errorf so you can report many problems at once. This makes it easier to fix multiple problems without rerunning your tests over and over.

### Logging

It is often helpful to output additional information when running tests. Go provides access to the testing logger via a set of methods on *`testing.T`. While you can use `fmt.Println` and `fmt.Printf`, it is better to use the testing logger because its output is only displayed when a test fails (or when you turn on verbose output).

The most commonly-used test logging methods are Log and Logf, which provide unformatted and formatted output. The log message is indented and prefixed with the file name and line number of the log statement.

If your log output is processed by external tools, you can include structured data in your output with the Attr method. It takes two string parameters, a key and a value. The meaning of the key/value pair is up to you; the only limitation that the key cannot contain any whitespace characters. The method writes a line with the following values, separated by whitespace: === ATTR, the name of the test, the key, and the value.

Finally, the Output method provides access to the test logger’s underlying `io.Writer`. Like Log and Logf, anything written using this `io.Writer` is indented, but there’s no file name/line number prefix.

```go
func TestLogging(t *testing.T) {
    fmt.Println("fmt.Println does work, but it's always there and unindented")
    t.Log("This is a simple string message")
    t.Logf("This message has %d %s specifiers in it", 2, "formatting")
    t.Attr("key_for_processing", "value_for_processing with whitespace")
    t.Output().Write([]byte("a final entry"))
}
```

Here’s the output for this test:

```console
$ go test -v
=== RUN   TestLogging
fmt.Println does work, but it's always there and unindented
    logging_test.go:10: This is a simple string message
    logging_test.go:11: This message has 2 formatting specifiers in it
=== ATTR  TestLogging key_for_processing value_for_processing with whitespace
    a final entry
--- PASS: TestLogging (0.00s)
PASS
ok      github.com/learning-go-book-3e/ch15/sample_code/logging 0.204s
```

### Saving Test Artifacts

It is sometimes useful to capture output files from a test (for additional analysis, perhaps). Instead of hard-coding a location into your test code, you can take advantage of Go’s artifact directory support. Use the ArtifactDir method to get the name of the directory where the file should be written. By default, this is a temporary directory that is deleted when the test completes. This gives you control over when an artifact is permanently written; the code to generate the artifact can always be present, but you decide when to capture a new artifact. To make an artifact permanent, set the -artifacts flag when running go test. This changes the artifact directory to a subdirectory of the directory where go test is running.

```go
func TestArtifacts(t *testing.T) {
    myDir := t.ArtifactDir()
    t.Log(myDir)
    f, err := os.Create(myDir + "/test.txt")
    if err != nil {
        t.Fatal(err)
    }
    defer f.Close()
    f.Write([]byte("valuable test data"))
}
```

```console
$ go test -v
=== RUN   TestArtifacts
    artifact_test.go:10: /var/folders/hj/mr53lrfj1bqf4hg62wqkp4000000gn/T/
        TestArtifacts1377298058/001
--- PASS: TestArtifacts (0.00s)

$ go test -v -artifacts
=== RUN   TestArtifacts
=== ARTIFACTS TestArtifacts /Users/gobook/projects/learning-go-3e-code/ch15/
        sample_code/artifact/_artifacts/1837011095
    artifact_test.go:10: /Users/gobook/projects/learning-go-3e-code/ch15/
        sample_code/artifact/_artifacts/1837011095
--- PASS: TestArtifacts (0.00s)
```

> **Note**
>
> If you want to customize the artifact output directory, set the -outputdir flag on go test.

### Setting Up and Tearing Down

Sometimes you have some common state that you want to set up before any tests run and remove when testing is complete. Use a TestMain function to manage this state and run your tests:

```go
var testTime time.Time

func TestMain(m *testing.M) {
    fmt.Println("Set up stuff for tests here")
    testTime = time.Now()
    exitVal := m.Run()
    fmt.Println("Clean up stuff after tests here")
    os.Exit(exitVal)
}

func TestFirst(t *testing.T) {
    slog.Info("TestFirst uses stuff set up in TestMain", testTime)
}

func TestSecond(t *testing.T) {
    slog.Info("TestSecond also uses stuff set up in TestMain", testTime)
}
```

Both TestFirst and TestSecond refer to the package-level variable testTime. Assume that it needs to be initialized in order for the tests to run properly. You declare a function called TestMain with a parameter of type *`testing.M`. If there’s a function named TestMain in a package, go test calls it instead of the test functions. It is the responsibility of the TestMain function to set up any state that’s necessary to make the tests in the package run correctly.

Once the state is configured, the TestMain function calls the Run method on *`testing.M`. This runs the test functions in the package. The Run method returns the exit code; 0 indicates that all tests passed. Finally, the TestMain function must call `os.Exit` with the exit code returned from Run.

Running go test on this produces the output:

```console
$ go test
Set up stuff for tests here
TestFirst uses stuff set up in TestMain 2026-03-30 23:10:55.190364 -0400 EDT
    m=+0.000474084
TestSecond also uses stuff set up in TestMain 2026-03-30 23:10:55.190364 -0400
    EDT m=+0.000474084
PASS
Clean up stuff after tests here
ok      test_examples/testmain  0.006s
```

> **Note**
>
> Be aware that TestMain is invoked once, not before and after each individual test. You can have only one TestMain per package.

TestMain is useful in two common situations:

- When you need to set up data in an external repository, such as a database

- When the code being tested depends on package-level variables that need to be initialized

As I’ve mentioned before (and will again!), you should avoid package-level variables in your programs. They make it hard to understand how data flows through your program. If you are using TestMain for this reason, consider refactoring your code.

### Cleanup, Context, and Helper

The Cleanup method on *`testing.T` is used to clean up temporary resources created for a single test. This method has a single parameter: a function with no input parameters or return values. The function runs when the test completes. For simple tests, you can achieve the same result by using a defer statement, but Cleanup is useful when tests rely on helper functions to set up sample data. It’s fine to call Cleanup multiple times. Just like defer, the functions are invoked in last-added, first-called order. Example 6-1 demonstrates a test helper function that uses Cleanup:

**Example 6-1. A Test Helper with t.Cleanup and t.Helper**

```go
func TestAddressQuery(t *testing.T) {
	db := setupDB(t, "address")
	address, err := FindAddress(t.Context(), db, "Fred")
	if err != nil {
		t.Error(err)
	}
	if address.Country != "Australia" {
		t.Error("wrong country")
	}
}

func setupDB(t *testing.T, tableName string) *sql.DB {
	t.Helper()
	db, err := sql.Open("ramsql", tableName)
	if err != nil {
		t.Fatal("error creating database", err)
	}
	t.Cleanup(func() { db.Close() })
	return db
}
```

Functions like setupDB are referred to as test helpers since they set up or tear down the state needed to properly test code, but do no testing themselves. If something goes wrong it is usually a fatal error, as the test cannot continue without valid initial conditions. To mark the function as a test helper, it is idiomatic to pass a *`testing.T` instance to these functions and add a call to `t.Helper` as the first line. When `t.Helper` is called, it modifies the output of any calls to `t.Error` or `t.Fatal` within the test helper. Rather than print the filename and line number of the line in the test helper, the filename and line number of the line in the test function that called the test helper is displayed. This is useful when a helper function is called from multiple tests; you’ll see the name of the test and the line where the helper was called in the error output.

In this example, the helper function setupDB creates a per-test database connection. Inside of setupDB, Cleanup is called to close the database connection when the test exits. We can’t use a defer here, because defer runs when a function exits and we want to close the connection when the test ends.

Another thing to notice is in TestAddressQuery. The context that’s passed into FindAddress comes from the `t.Context` method. This is a special context that is automatically canceled when the test exits. Using it allows any code being tested to shut down properly when the test ends. Prefer using `t.Context` in tests over `context.Background`.

You can find this sample code in the `sample_code/helper` directory in the Chapter 15 repository has an example. It is also available on the Go Playground. Change "ramsql" to some other string and run the test with the `t.Helper`() line commented and then uncommented to see the difference it makes in the error output.

### Working with Temporary Directories

If your test uses temporary files, use the `t.TempDir` method. It creates a new temporary directory every time it is invoked and returns the full path of the directory. It also registers a handler with Cleanup to delete the directory and its contents when the test completes. Example 6-2 demonstrates its usage:

**Example 6-2. Using t.TempDir**

```go
// createFile is a helper function called from multiple tests
func createFile(t *testing.T) string {
	t.Helper()
	tempDir := t.TempDir()

	f, err := os.CreateTemp(tempDir, "tempFile")
	if err != nil {
		t.Fatal("error creating temp file", err)
	}
	defer f.Close()
	// write some data to f
	f.Write([]byte("Hello"))
	return f.Name()
}

func TestFileProcessing(t *testing.T) {
	fName := createFile(t)
	// do testing, don't worry about cleanup
}
```

You can find this example in the `sample_code/tempdir` directory in the Chapter 15 repository or on the Go playground.

### Testing with Environment Variables

It’s a common (and very good) practice to configure applications with environment variables. To simplify writing tests for code that depends on environment variables, Go provides a helper method on `testing.T`. Call `t.Setenv` to register a value for an environment variable for your test. Behind the scenes, it calls Cleanup to revert the environment variable to its previous state when the test exits:

```go
// assume ProcessEnvVars is a function that processes environment variables
// and returns a struct with an OutputFormat field
func TestProcessEnvVar(t *testing.T) {
    t.Setenv("OUTPUT_FORMAT", "JSON")
    cfg := ProcessEnvVars()
    if cfg.OutputFormat != "JSON" {
        t.Error("OutputFormat not set correctly")
    }
    // value of OUTPUT_FORMAT is reset when the test function exits
}
```

> **Note**
>
> While it is good to use environment variables to configure your application, it is also good to make sure that most of your code is entirely unaware of them. Be sure to copy the values of environment variables into configuration structs before your program starts its work, in your main function or soon afterward. Doing so makes it easier to reuse and test code, since how the code is configured has been abstracted away from what the code is doing.

Rather than writing this code yourself, you should strongly consider using a third-party configuration library, like Viper or envconfig. Also, look at GoDotEnv as a way to store environment variables in .env files for development or continuous integration machines.

### Storing Sample Test Data

As go test walks your source code tree, it uses the current package directory as the current working directory. If you want to use sample data to test functions in a package, create a subdirectory named `testdata` to hold your files. Go reserves this directory name as a place to hold test files. When reading from `testdata`, always use a relative file reference. Since go test changes the current working directory to the current package, each package accesses its own `testdata` via a relative file path.

> **Tip**
>
> The text package in the sample_code directory of the Chapter 15 repository demonstrates how to use `testdata`.

### Caching Test Results

As you learned in Chapter 10, Go caches compiled packages if they haven’t changed. Go also caches test results when running tests across multiple packages if they have passed and their code hasn’t changed. The tests are recompiled and rerun if you change any file in the package or in the `testdata` directory. You can also force tests to always run if you pass the flag -count=1 to go test.

### Testing Your Public API

The tests that you’ve written are in the same package as the production code. This allows you to test both exported and unexported functions.

If you want to test just the public API of your package, Go has a convention for specifying this. You still keep your test source code in the same directory as the production source code, but you use packagename_test for the package name. Let’s redo the initial test case, using an exported function instead. You can find the code in the `sample_code/pubadder` directory in the Chapter 15 repository. In the adder_public.go file in pubadder package, the following exported function is declared:

```go
func AddNumbers(x, y int) int {
    return x + y
}
```

You test the function as public API by using the following code in a file in the pubadder directory named `adder_public_test.go`:

```go
package pubadder_test

import (
    "github.com/learning-go-book-3e/ch15/sample_code/pubadder"
    "testing"
)

func TestAddNumbers(t *testing.T) {
    result := pubadder.AddNumbers(2, 3)
    if result != 5 {
        t.Error("incorrect result: expected 5, got", result)
    }
}
```

Notice that the package name for the test file is pubadder_test. You have to import github.com/learning-go-book-3e/ch15/`sample_code/pubadder` even though the files are in the same directory. To follow the convention for naming tests, the test function name matches the name of the AddNumbers function. Also note that you use pubadder.AddNumbers, since you are calling an exported function in a different package.

Just as you can call exported functions from within a package, you can test your public API from a test that is in the same package as your source code. The advantage of using the _test suffix in the package name is that it lets you treat your tested package as a “black box.” You are forced to interact with it only via its exported functions, methods, types, constants, and variables.

> **Tip**
>
> A package can include test source files that use the _test suffix for the package declaration alongside test source files that use the package name. This allows you to organize your tests for exported and unexported functions into different files.

### Tests and the Context

When writing tests for functions that expect a context (as covered in Chapter 14), don’t use `context.Background` to generate a context. Instead, use `t.Context`. This returns a context that is automatically canceled when the test exits (if you registered any functions with `t.Cleanup`, the context is cancelled just before they run). Using the test context allows any code under test to properly shut down. This includes goroutines that exit upon context cancellation. (In “Test Concurrent Code with synctest”, you will learn how to find goroutines that don’t shut down when the context is canceled.) Sample code that demonstrates the test context is in the `sample_code/oracle` directory in the Chapter 15 repository:

```go
func TestOracle(t *testing.T) {
    ctx := t.Context()
    ch := oracle.Launch(ctx)
    outCh := make(chan string)
    ch <- oracle.Request{
        Query:    "Is the sky blue?",
        Response: outCh,
    }
    result := <-outCh
    if result != "Is the sky blue? Yes!" {
        t.Error("the oracle is wearing rose-tinted glasses")
    }
}
```

### Using go-cmp to Compare Test Results

Writing a thorough comparison of a compound type’s two instances can be verbose. While you can use `reflect.DeepEqual` to compare structs, maps, and slices, there’s a better way. Back in 2017, Google released a third-party module called go-cmp that does the comparison for you and returns a detailed description of what does not match. Let’s see how it works by defining a simple struct and a factory function that populates it. You can find this code in the `sample_code/cmp` directory in the Chapter 15 repository:

```go
type Person struct {
    Name      string
    Age       int
    DateAdded time.Time
}

func CreatePerson(name string, age int) Person {
    return Person{
        Name:      name,
        Age:       age,
        DateAdded: time.Now(),
    }
}
```

In your test file, import github.com/google/go-cmp/cmp. The test function looks like this:

```go
func TestCreatePerson(t *testing.T) {
    expected := Person{
        Name: "Dennis",
        Age:  37,
    }
    result := CreatePerson("Dennis", 37)
    if diff := cmp.Diff(expected, result); diff != "" {
        t.Error(diff)
    }
}
```

The `cmp.Diff` function takes in the expected output and the output that was returned by the function that you’re testing. It returns a string that describes any mismatches between the two inputs. If the inputs match, it returns an empty string. You assign the output of the `cmp.Diff` function to a variable called diff and then check whether diff is an empty string. If it is not, an error occurred.

When you build and run the test, you’ll see the output that go-cmp generates when two struct instances don’t match:

```console
$ go test
--- FAIL: TestCreatePerson (0.00s)
    ch13_cmp_test.go:16:   ch13_cmp.Person{
              Name:      "Dennis",
              Age:       37,
        -     DateAdded: s"0001-01-01 00:00:00 +0000 UTC",
        +     DateAdded: s"2020-03-01 22:53:58.087229 -0500 EST m=+0.001242842",
          }

FAIL
FAIL    ch13_cmp    0.006s
```

The lines with a - and + indicate the fields whose values differ. The test failed because the dates didn’t match. This is a problem because you can’t control what date the CreatePerson function assigns. You have to ignore the DateAdded field. The go-cmp module includes a helper package, cmpopts, which contains functions that provide additional control over the comparisons performed by `cmp.Diff`. In this case, use `cmpopts.IgnoreFields` to (unsurprisingly) ignore a field:

```go
if diff := cmp.Diff(expected,
                    result,
                    cmpopts.IgnoreFields(Person{}, "DateAdded")); diff != "" {
    t.Error(diff)
}
```

This is only a quick preview of the most useful features in go-cmp. Check its documentation to learn more about how to control what is compared and the output format.

### Running Table Tests

Most of the time, it takes more than a single test case to validate that a function is working correctly. You could write multiple test functions to validate your function or multiple tests within the same function, but you’ll find that a great deal of the testing logic is repetitive. You set up supporting data and functions, specify inputs, check the outputs, and compare to see if they match your expectations.

Rather than writing this over and over, you can take advantage of a pattern called table tests. Let’s take a look at a sample. You can find this code in the `sample_code/table` directory in the Chapter 15 repository. Assume you have the following function in the table package:

```go
func DoMath(num1, num2 int, op string) (int, error) {
    switch op {
    case "+":
        return num1 + num2, nil
    case "-":
        return num1 - num2, nil
    case "*":
        return num1 + num2, nil
    case "/":
        if num2 == 0 {
            return 0, ErrDivZero
        }
        return num1 / num2, nil
    default:
        return 0, &UnknownOpErr{Op: op}
    }
}
```

To test this function, you need to check the different branches, trying out inputs that return valid results, as well as inputs that trigger errors. You could write code like this, but it would be very repetitive:

```go
func TestDoMath(t *testing.T) {
    result, err := DoMath(2, 2, "+")
    if result != 4 {
        t.Error("Should have been 4, got", result)
    }
    if err != nil {
        t.Error("Should have been nil error, got", err)
    }
    result2, err2 := DoMath(2, 2, "-")
    if result2 != 0 {
        t.Error("Should have been 0, got", result2)
    }
    if err2 != nil {
        t.Error("Should have been nil error, got", err2)
    }
    // and so on...
}
```

Let’s replace this repetition with a table test. First, declare a slice of anonymous structs. The struct contains fields for the name of the test, the input parameters, and the return values. Each entry in the slice represents another test:

```go
data := []struct {
    name     string
    num1     int
    num2     int
    op       string
    expected int
    err      error
}{
    {"addition", 2, 2, "+", 4, nil},
    {"subtraction", 2, 2, "-", 0, nil},
    {"multiplication", 2, 2, "*", 4, nil},
    {"division", 2, 2, "/", 1, nil},
    {"bad_division", 2, 0, "/", 0, ErrDivZero},
}
```

Next, loop over each test case in data, invoking the Run method each time. This is the line that does the magic. You pass two parameters to Run, a name for the subtest and a function with a single parameter of type *`testing.T`. Inside the function, you call DoMath by using the fields of the current entry in data, using the same logic over and over. When you run these tests, you’ll see that not only do they pass, but when you use the -v flag, each subtest also now has a name:

```go
for _, d := range data {
    t.Run(d.name, func(t *testing.T) {
        result, err := DoMath(d.num1, d.num2, d.op)
        if result != d.expected {
            t.Errorf("Expected %d, got %d", d.expected, result)
        }
        if !errors.Is(err, d.err) {
            t.Errorf("expected %v, got %v", d.err, err)
        }
    })
}
```

> **Tip**
>
> Comparing error messages in tests is fragile, because there may not be any compatibility guarantees on the message text. If you are testing code that uses `errors.New` and `fmt.Errorf` to make errors, you have three options: limit your testing to whether or not the returned error is nil, rewrite your code to use custom error types and sentinel errors, or compare the messages and hope for the best. It’s best to re-write your code.

### Running Tests Concurrently

By default, unit tests are run sequentially. Since each unit test is supposed to be independent from every other unit test, they make ideal candidates for concurrency. To make a unit test run concurrently with other tests, call the Parallel method on *`testing.T` as the first line in your test:

```go
func TestMyCode(t *testing.T) {
    t.Parallel()
    // rest of test goes here
}
```

Parallel tests run concurrently with other tests marked as parallel. The Go runtime manages this for you automatically; there’s no exposed configuration.

You can also call Parallel from within a table test:

```go
func TestParallelTable(t *testing.T) {
    data := []struct {
        name   string
        input  int
        output int
    }{
        {"a", 10, 20},
        {"b", 30, 40},
        {"c", 50, 60},
    }
    for _, d := range data {
        t.Run(d.name, func(t *testing.T) {
            t.Parallel()
            t.Log(d.input, d.output)
            out := toTest(d.input)
            if out != d.output {
                t.Error("didn't match", out, d.output)
            }
        })
    }
}
```

The table test subtests run in parallel with each other, but the parent test blocks until all of the subtests complete.

You can run this code on The Go Playground or in the `sample_code/parallel` directory in the Chapter 15 repository.

The advantage of parallel tests is they can speed up long-running test suites. There are some disadvantages, though. If you have multiple tests that rely on the same shared mutable state, do not mark them as parallel, because you will get inconsistent results. (But after all of my warnings, you don’t have any shared mutable state in your application, right?) Also be aware that your test will panic if you mark it as parallel and use the Setenv method in your test function.

> **Note**
>
> Go 1.22 (released in February, 2024) changed the lifecycle of the index and value variables in for loops. The compiler now creates a new copy of the index and value variables on each iteration if there’s any chance they could be captured by a closure. This eliminated bugs in parallel tests that were using shared index and value state. If you are still using Go 1.21 or earlier (or have the Go version in the go directive in your `go.mod` file set to 1.2.1 or earlier), I strongly recommend upgrading to take advantage of this improved behavior.

Now that you have a way to run lots of tests, you’ll learn about code coverage to find out what your tests are testing.

## Code Review: Basic Testing

- Take advantage of Go’s built-in testing framework to write idiomatic tests.

- Make sure that tests cover positive and negative cases.

- Use the `testdata` directory to hold data for running your tests.

- Use `t.Context`() instead of `context.Background`().

- Consider whether go-cmp would simplify comparisons.

- Use table tests to validate the same logic with different data.

- If your tests are independent (and they should be), use `t.Parallel`().

## Exercises

These exercises help you practice the basics of Go testing. They are found in the exercises directory in the Chapter 15 repository. Solutions are in the `exercise-solutions` directory in the Chapter 15 repository.

1. In the ex1 directory, there is a file called calculator.go, with a function called Average. Create a `calculator_test.go` file with a function to test Average. If you find a bug in the function, fix the bug and confirm that the test passes.

2. In the ex2 directory, there is a file called temperature.go with a function called Convert. Create a `temperature_test.go` file with a function that uses a table test to validate all inputs and possible errors. If you find a bug in the function, fix the bug and confirm that the test passes.

3. In the ex3 directory, there is a file called counter.go with a function called TotalFile. Create a `counter_test.go` file with a function to test TotalFile. Use a helper function to create both good and bad sample data.

## Checking Your Code Coverage

Code coverage is a very useful tool for knowing whether you’ve missed any obvious cases. However, reaching 100% code coverage doesn’t guarantee that there aren’t bugs in your code for some inputs. First you’ll see how go test displays code coverage and then you’ll look at the limitations of relying on code coverage alone.

Adding the -cover flag to the go test command calculates coverage information and includes a summary in the test output. If you include a second flag -coverprofile, you can save the coverage information to a file. Let’s go back to the `sample_code/table` directory in the Chapter 15 repository and gather code coverage information:

```console
$ go test -v -cover -coverprofile=c.out
```

If you run your table test with code coverage, the test output now includes a line that indicates the amount of test code coverage, 87.5%. That’s good to know, but it’d be more useful if you could see what you missed. The cover tool included with Go generates an HTML representation of your source code with that information:

```console
$ go tool cover -html=c.out
```

When you run it, your web browser opens and shows you a page with code coverage information using a dark mode color scheme. Every file that’s tested appears in the combo box in the upper left. The source code is in one of three colors. Gray is used for lines of code that aren’t testable, green is used for code that’s been covered by a test, and red is used for code that hasn’t been tested. This reliance on color is unfortunate for those who have red-green color blindness (and those whose publishers don’t want to print large blocks of black ink). To address this issue, I have created a fork of the cover tool. Install and run it with:

```console
$ go install github.com/jonbodner/coverlight@latest
$ coverlight -html c.out
```

The page that opens should look similar to Figure 6-1. Code with test coverage is displayed in black, code without test coverage is displayed as white text with a black background, and gray is used for untestable lines of code. From looking at this, you can see that you didn’t write a test to cover the default case, when a bad operator is passed to your function. Add that case to your slice of test cases:

```go
{"bad_op", 2, 2, "?", 0, &UnknownOpErr{Op: "?"}},
```

When you rerun go test -v -cover -coverprofile=c.out and coverlight -html c.out, you see in Figure 6-2 that the final line in DoMath is covered. There is still missing code coverage for the methods for UnknownOppErr. I’ll leave it as an exercise for the reader to write an additional test to get 100% test code coverage.

**Initial Code Coverage for DoMath**

*Figure 6-1. Initial code coverage*

**Final Code Coverage for DoMath**

*Figure 6-2. Final code coverage*

Code coverage is a great thing, but it’s not enough. There’s actually a bug in your code, even though you have 100% coverage. Have you noticed it? If not, add another test case and rerun your tests:

```go
{"another_mult", 2, 3, "*", 6, nil},
```

You should see the error:

```text
table_test.go:60: Expected 6, got 5
```

Your case for multiplication has a typo. It adds the numbers together instead of multiplying them. (Beware the dangers of copy-and-paste coding!) Fix the code, rerun go test -v -cover -coverprofile=c.out and go tool cover -html=c.out, and you’ll see that the tests pass again.

> **Warning**
>
> Code coverage is necessary but not sufficient. You can have 100% code coverage and still have bugs in your code!

## Fuzzing

One of the most important lessons that every developer eventually learns is that all data is suspect. No matter how well specified a data format is, you will eventually have to process input that doesn’t match what you expect. This doesn’t happen for only malicious reasons. Data can be corrupted in transit, in storage, and even in memory. Programs that process data might have bugs, and specifications for data formats always have corner cases that developers interpret in different ways.

Even when developers do the work of writing good unit tests, it’s impossible to think of everything. As you’ve seen, even 100% unit test code coverage is no guarantee that your code is bug free. You need to supplement unit tests with generated data that could break your program in ways you didn’t anticipate. That’s where fuzzing helps.

Fuzzing is a technique for generating random data and submitting it to code to see whether it properly handles unexpected input. The developer can provide a seed corpus or set of known good data, and the fuzzer uses that as a basis for generating bad input. Let’s see how to use the fuzzing support in Go’s testing tools to discover additional test cases.

Assume that you are writing a program to process data files. You can find the code for this example on GitHub. You are sending a list of strings but want to efficiently allocate memory, so the number of strings in a file is sent as the first line, while the remaining lines are the lines of text. Here’s the sample function for processing this data:

```go
func ParseData(r io.Reader) ([]string, error) {
    s := bufio.NewScanner(r)
    if !s.Scan() {
        return nil, ErrEmpty
    }
    countStr := s.Text()
    count, err := strconv.Atoi(countStr)
    if err != nil {
        return nil, &ParseError{CountStr: countStr}
    }
    out := make([]string, 0, count)
    for range count {
        hasLine := s.Scan()
        if !hasLine {
            return nil, ErrTooFewLines
        }
        line := s.Text()
        out = append(out, line)
    }
    return out, nil
}
```

You use a bufio.Scanner to read line-by-line from an `io.Reader`. If there’s no data to be read, an error is returned. You then read the first line and attempt to convert it to an int named count. If you can’t, an error is returned. Next, you allocate the memory for your slice of strings, and read count number of lines from the scanner. If there aren’t enough lines, an error is returned. If all goes well, you return the lines you read.

A unit test has already been written to validate the code:

```go
func TestParseData(t *testing.T) {
    data := []struct {
        name string
        in   []byte
        out  []string
        err  error
    }{
        {
            name: "simple",
            in:   []byte("3\nhello\ngoodbye\ngreetings\n"),
            out:  []string{"hello", "goodbye", "greetings"},
            err:  nil,
        },
        {
            name: "empty_error",
            in:   []byte(""),
            out:  nil,
            err:  ErrEmpty,
        },
        {
            name: "zero",
            in:   []byte("0\n"),
            out:  []string{},
            err:  nil,
        },
        {
            name: "number_error",
            in:   []byte("asdf\nhello\ngoodbye\ngreetings\n"),
            out:  nil,
            err:  &ParseError{CountStr: "asdf"},
        },
        {
            name: "line_count_error",
            in:   []byte("4\nhello\ngoodbye\ngreetings\n"),
            out:  nil,
            err:  ErrTooFewLines,
        },
    }
    for _, d := range data {
        t.Run(d.name, func(t *testing.T) {
            r := bytes.NewReader(d.in)
            out, err := ParseData(r)
            if !errors.Is(err, d.err) {
                t.Errorf("expected %v, got %v", d.err, err)
            }
            if diff := cmp.Diff(d.out, out); diff != "" {
                t.Error(diff)
            }
        })
    }
}
```

The unit test has 100% line coverage for ParseData, handling all its error cases. You might think the code is ready for production, but let’s see if fuzzing can help you discover errors that you hadn’t considered.

> **Note**
>
> Be aware that fuzzing uses a lot of resources. A fuzz test can allocate (or attempt to allocate) many gigabytes of memory and might write several gigabytes of data to your local disk. If you are running something else on the same machine at the same time as a fuzz test, don’t be surprised if it slows down.

Start by writing a fuzz test:

```go
func FuzzParseData(f *testing.F) {
    testcases := [][]byte{
        []byte("3\nhello\ngoodbye\ngreetings\n"),
        []byte("0\n"),
    }
    for _, tc := range testcases {
        f.Add(tc) // Use f.Add to provide a seed corpus
    }
    f.Fuzz(func(t *testing.T, in []byte) {
        r := bytes.NewReader(in)
        out, err := ParseData(r)
        if err != nil {
            t.Skip("handled error")
        }
        roundTrip := ToData(out)
        rtr := bytes.NewReader(roundTrip)
        out2, _ := ParseData(rtr)
        if diff := cmp.Diff(out, out2); diff != "" {
            t.Error(diff)
        }
    })
}
```

A fuzz test looks similar to a standard unit test. The function name starts with Fuzz, the only parameter is of type *`testing.F`, and it has no return values.

Next, set up a seed corpus, which is composed of one or more sets of sample data. The data can run successfully, error out, or even panic. The important things are that you know how your program behaves when this data is provided and that this behavior is accounted for by your fuzz test. These samples are mutated by the fuzzer to generate bad inputs. This example uses only a single field of data for each entry (a slice of bytes), but you can have as many fields as needed. The fields in a corpus entry are currently limited to only certain types:

- Any integer type (including unsigned types, rune, and byte)

- Any floating-point type

- bool

- string

- []byte

Each entry in the corpus is passed to the Add method on the *`testing.F` instance. In the example, you have a slice of bytes for each entry:

```go
f.Add(tc)
```

If the function being fuzzed needed an int and a string, the call to Add would look like this:

```go
f.Add(1, "some text")
```

It’s a runtime error to pass a value of an invalid type to Add.

Next, call the Fuzz method on your *`testing.F` instance. This looks a bit like a call to Run when writing a table test in a standard unit test. Fuzz takes in a single parameter, a function whose first parameter is of type *`testing.T` and whose remaining parameters exactly match the types, order, and count of the values that were passed in to Add. This also specifies the type of data generated by the fuzzing engine during fuzzing. There’s no way for the Go compiler to enforce this constraint, so it’s a runtime error if the convention is not followed.

Finally, let’s look at the body of the fuzz target. Remember, fuzzing is used to find cases where bad input is not handled correctly. Since the input is randomly generated, you can’t write tests that have knowledge of what the output should be. Instead, you have to use test conditions that will be true for all inputs. In the case of ParseData, you can check for two things:

- Does the code return an error for bad input, or does it panic?

- If you convert the slice of strings back to a slice of bytes and re-parse it, do you get the same result?

Let’s see what happens when you run the fuzz test:

```console
$ go test -fuzz=FuzzParseData
fuzz: elapsed: 0s, gathering baseline coverage: 0/137 completed
failure while testing seed corpus entry: FuzzParseData/03f81b404ad91d09
fuzz: elapsed: 3s, gathering baseline coverage: 2/137 completed
--- FAIL: FuzzParseData (2.92s)
    --- FAIL: FuzzParseData (0.00s)
        testing.go:1927: panic: runtime error: makeslice: cap out of range
            goroutine 12 [running]:
            runtime/debug.Stack()
                /opt/homebrew/opt/go/libexec/src/runtime/debug/stack.go:26 +0xc4
            testing.tRunner.func1()
                /opt/homebrew/opt/go/libexec/src/testing/testing.go:1927 +0x218
            panic({0x100ca49c0?, 0x100ce5dc0?})
                /opt/homebrew/opt/go/libexec/src/runtime/panic.go:860 +0x12c
            file_parser.ParseData({0x100ce7a40?, 0x10e411dfcf30?})
                file_parser/file_parser.go:46 +0x134
```

If you don’t specify the -fuzz flag, your fuzz tests will be treated like unit tests and will be run against the seed corpus. Only a single fuzz test can be fuzzed at a time.

> **Note**
>
> If you want to get the full experience, delete the contents of the `testdata/fuzz/FuzzParseData` directory. This will cause the fuzzer to generate new seed corpus entries. Since the fuzzer generates random input, your samples might be different from the ones shown. The different entries will likely produce similar errors, though maybe not in the same order.

The fuzz test runs and in less than a second, it reports a panic. Panics are bad, so let’s look at the input that was generated. Every time a test case fails, the fuzzer writes it to the `testdata/fuzz/TESTNAME` subdirectory in the same package as the failed test, adding a new entry to the seed corpus. This automatically generated unit test runs when go test -fuzz=FuzzParseData is called, and acts as a regression test once you fix your bug.

Here are the contents of the file:

```text
go test fuzz v1
[]byte("-1")
```

The first line is a header to indicate that this is test data for a fuzz test. The subsequent lines have the data that caused the failure.

Passing the name of the file in the failure message as a -run parameter to go test allows you to isolate this failing case when you rerun the test:

```console
$ go test -run=FuzzParseData/03f81b404ad91d09
--- FAIL: FuzzParseData (0.00s)
    --- FAIL: FuzzParseData/03f81b404ad91d09 (0.00s)
panic: runtime error: makeslice: cap out of range [recovered, repanicked]
```

The line that’s generating the panic is shown here:

```go
out := make([]string, 0, count)
```

You are trying to create a slice with negative capacity, which panics. An error type for this situation has been handily defined for you. Add a condition to your code to look for negative numbers before you call make:

```go
if count < 0 {
    return nil, ErrNegative
}
```

If you run go test -run=FuzzParseData/03f81b404ad91d09, you’ll see that the test now passes. Run the fuzzer again to see whether it finds any more errors:

```console
$ go test -fuzz=FuzzParseData
fuzz: elapsed: 0s, gathering baseline coverage: 0/137 completed
failure while testing seed corpus entry: FuzzParseData/0e4ad8073b1a5373
fuzz: elapsed: 3s, gathering baseline coverage: 2/137 completed
--- FAIL: FuzzParseData (2.95s)
    --- FAIL: FuzzParseData (0.00s)
        file_parser_test.go:87:   []string{
              ... // 3 identical elements
              "",
              "",
            -  "\r",
            +  "",
              "0",
            }
```

This time, the input file created by the fuzzer looks like this:

```text
go test fuzz v1
[]byte("7\n\n\n\n\n\n\r\r\n0")
```

The fuzz test is generating blank lines with \r (return) characters. Blank lines are not expected in your input, so add some code to the loop that reads lines of text from the Scanner. You’ll check whether a line consists only of whitespace characters. If it does, return an error:

```go
line = strings.TrimSpace(line)
if len(line) == 0 {
    return nil, ErrBlankLine
}
```

Validate that you fixed the bug with go test -run=FuzzParseData/0e4ad8073b1a5373, then run the fuzzer again to see whether it finds any more errors:

```console
$ go test -fuzz=FuzzParseData
fuzz: elapsed: 0s, gathering baseline coverage: 0/137 completed
fuzz: elapsed: 3s, gathering baseline coverage: 136/137 completed
fuzz: elapsed: 6s, gathering baseline coverage: 136/137 completed
fuzz: elapsed: 9s, gathering baseline coverage: 136/137 completed
failure while testing seed corpus entry: FuzzParseData/e8bf251ff804c663
fuzz: elapsed: 11s, gathering baseline coverage: 136/137 completed
--- FAIL: FuzzParseData (10.83s)
    fuzzing process hung or terminated unexpectedly: exit status 2
```

In this case, the go command reports that your program has “hung or terminated unexpectedly”. We don’t want programs to hang or terminate, expectedly or unexpectedly, so let’s look at the generated test case to figure out what went wrong:

```text
go test fuzz v1
[]byte("3000000000000")
```

The problem is that you are trying to allocate a slice with the capacity to hold 3 trillion strings. That requires quite a bit more RAM than my computer (and probably yours) has. You need to limit the number of expected text elements to a reasonable number. Use the sentinel error ErrTooManyLines and set the maximum number of rows to 1,000 by adding the following code to ParseData after you parse the number of expected rows:

```go
if count > 1000 {
    return nil, ErrTooManyLines
}
```

Validate that the bug is fixed with go test -run=FuzzParseData/e8bf251ff804c663, and run the fuzzer yet again:

```console
$ go test -fuzz=FuzzParseData
fuzz: elapsed: 0s, gathering baseline coverage: 0/147 completed
fuzz: elapsed: 0s, gathering baseline coverage: 147/147 completed,
    now fuzzing with 16 workers
fuzz: elapsed: 3s, execs: 1568753 (522795/sec), new interesting: 1 (total: 148)
fuzz: elapsed: 6s, execs: 3134921 (522087/sec), new interesting: 1 (total: 148)
fuzz: elapsed: 9s, execs: 4652294 (505854/sec), new interesting: 1 (total: 148)
...
fuzz: elapsed: 2m9s, execs: 59383661 (416674/sec), new interesting: 2 (total: 149)
fuzz: elapsed: 2m12s, execs: 60694659 (436957/sec), new interesting: 3 (total: 150)
fuzz: elapsed: 2m15s, execs: 61976072 (427059/sec), new interesting: 3 (total: 150)
^C
PASS
```

After a few minutes, no more errors are found, so hit Ctrl-C to end fuzzing. You can also use the -fuzztime flag to specify a time limit (-fuzztime=60s for a 60 second run) or a number of iterations (-fuzztime=100000x to run the fuzzer 100,000 times).

Just because the fuzzer didn’t find additional issues doesn’t mean that the code is now bug free. However, fuzzing allowed you to automatically find some significant oversights in the original code. Writing fuzz tests takes practice, as they require a slightly different mindset than writing unit tests. Once you get the hang of them, they become an essential tool for validating how your code handles unexpected user input. Once you have a library of fuzz tests, run them periodically on your CI infrastructure, using -fuzztime to timebox the work.

## Using Benchmarks

Determining how fast (or slow) code runs is surprisingly difficult. Rather than trying to figure it out yourself, use the benchmarking support that’s built into Go’s testing framework. Let’s explore it with a function in the `sample_code/bench` directory in the Chapter 15 repository:

```go
func FileLen(f string, bufsize int) (int, error) {
    file, err := os.Open(f)
    if err != nil {
        return 0, err
    }
    defer file.Close()
    count := 0
    for {
        buf := make([]byte, bufsize)
        num, err := file.Read(buf)
        count += num
        if err != nil {
            break
        }
    }
    return count, nil
}
```

This function counts the number of characters in a file. It takes in two parameters, the name of the file and the size of the buffer that you are using to read the file (you’ll see the reason for the second parameter in a moment).

Before seeing how fast it is, test your library to make sure that it works:

```go
func TestFileLen(t *testing.T) {
    result, err := FileLen("testdata/data.txt", 1)
    if err != nil {
        t.Fatal(err)
    }
    if result != 65204 {
        t.Error("Expected 65204, got", result)
    }
}
```

The unit tests passes, so now it is time to see how long it takes your file-length function to run. The goal is to find out what size buffer you should use to read from the file.

> **Note**
>
> Before you spend time going down an optimization rabbit hole, be sure that you need to optimize. If your program is already fast enough to meet your responsiveness requirements and is using an acceptable amount of memory, your time is better spent on adding features and fixing bugs. Your business requirements determine what “fast enough” and “acceptable amount of memory” mean.

In Go, benchmarks are functions in your test files that start with the word Benchmark and take in a single parameter of type *`testing.B`. This type includes all the functionality of a *`testing.T` as well as additional support for benchmarking. Let’s start by looking at a benchmark that uses a buffer size of 1 byte:

```go
func BenchmarkFileLen1(b *testing.B) {
    for b.Loop() {
        _, err := FileLen("testdata/data.txt", 1)
        if err != nil {
            b.Fatal(err)
        }
    }
}
```

Go 1.24 introduced the Loop method on *`testing.B`. It manages three things that you had to do by hand in earlier versions of Go. The first is looping the proper number of times. The testing framework calls your benchmark functions repeatedly until it is sure that the timing results are accurate. Using `b.Loop` ensures this is done properly.

The second thing is `b.Loop` ensures that any code before or after the loop is automatically excluded from the benchmark measurement.

The final thing the `b.Loop` method does is it prevents optimization. Compilers are pretty smart. They can automatically remove calculations or function calls whose values are never used. This is fantastic when running a program in production, but it’s not so great if you are calling a function in a benchmark to see how fast it is and don’t care about the result. The compiler might remove the function call from the benchmark, which is not helpful.

In order to address this, the Go compiler has a special rule when it sees that it is compiling a benchmark with a for `b.Loop` loop. In that one case, it makes sure that nothing in the body of the for loop is removed from the compiled code.

You run a benchmark by passing the -bench flag to go test. This flag expects a regular expression to describe the name of the benchmarks to run. Use -bench=. to run all benchmarks. A second flag, -benchmem, includes memory allocation information in the benchmark output. All tests are run before the benchmarks, so you can benchmark code only when tests pass.

Here’s the output for the benchmark on my computer:

```text
BenchmarkFileLen1-16  44 24379298 ns/op  128 B/op  3 allocs/op
```

Running a benchmark with memory allocation information produces output with five columns. Here’s what each one means:

**BenchmarkFileLen1-16**

The name of the benchmark, a hyphen, and the value of `GOMAXPROCS` for the benchmark.

**44**

The number of times that the test ran to produce a stable result.

**24379298 ns/op**

The amount of time it took to run a single pass of this benchmark, in nanoseconds (there are a billion nanoseconds in a second).

**128 B/op**

The number of bytes allocated during a single pass of the benchmark.

**3 allocs/op**

The number of times bytes had to be allocated from the heap during a single pass of the benchmark. This will always be less than or equal to the number of bytes allocated.

As I covered in “Reducing the Garbage Collector’s Workload”, we care about the number of bytes allocated on the heap and the number of times that our program allocates from the heap, because heap allocations create more work for the garbage collector. The more time your program spends garbage collecting, the less time it spends doing the work you wrote it to do.

Now that you have results for a buffer of 1 byte, let’s see what the results look like when you use buffers of different sizes:

```go
func BenchmarkFileLen(b *testing.B) {
    for _, v := range []int{1, 10, 100, 1000, 10000, 100000} {
        b.Run(fmt.Sprintf("FileLen-%d", v), func(b *testing.B) {
            for b.Loop() {
                _, err := FileLen("testdata/data.txt", v)
                if err != nil {
                    b.Fatal(err)
                }
            }
        })
    }
}
```

Just as you launched table tests using `t.Run`, you’re using `b.Run` to launch benchmarks that vary based only on input. Here are the results of this benchmark on my computer:

```text
BenchmarkFileLen/FileLen-1-16          49  24230445 ns/op     128 B/op    3 allocs/op
BenchmarkFileLen/FileLen-10-16        489   2458019 ns/op     128 B/op    3 allocs/op
BenchmarkFileLen/FileLen-100-16      4214    269902 ns/op   73376 B/op  657 allocs/op
BenchmarkFileLen/FileLen-1000-16    29570     40574 ns/op   68736 B/op   70 allocs/op
BenchmarkFileLen/FileLen-10000-16   72368     16581 ns/op   82048 B/op   11 allocs/op
BenchmarkFileLen/FileLen-100000-16  62640     19032 ns/op  213121 B/op    5 allocs/op
```

Parts of these results are expected and parts are surprising. As you increase the size of the buffer, it takes fewer loops to read all the data and your code runs faster, until the buffer is bigger than the file. When the buffer is bigger than the size of the file, extra allocations slow the output. If you expect files of roughly this size, a buffer of 10,000 bytes works best.

In “Allocating Slices”, I mentioned that slices can sometimes be allocated on the stack instead of the heap; this benchmark provides a demonstration. The 1 byte and 10 byte buffers uses little heap memory because they are allocated on the stack. The benchmem flag only shows expensive heap allocations, not cheap stack allocations. For larger buffers, the heap is used.

But you can make a change that improves the numbers more. You are reallocating the buffer every time you get the next set of bytes from the file. That’s unnecessary. If you move the byte slice allocation before the loop and rerun your benchmark, you see an improvement:

```text
BenchmarkFileLen/FileLen-1-16          48  24040199 ns/op     128 B/op  3 allocs/op
BenchmarkFileLen/FileLen-10-16        490   2435033 ns/op     128 B/op  3 allocs/op
BenchmarkFileLen/FileLen-100-16      4680    255315 ns/op     240 B/op  4 allocs/op
BenchmarkFileLen/FileLen-1000-16    34837     34776 ns/op    1152 B/op  4 allocs/op
BenchmarkFileLen/FileLen-10000-16   93732     12751 ns/op   10368 B/op  4 allocs/op
BenchmarkFileLen/FileLen-100000-16  84337     14236 ns/op  106624 B/op  4 allocs/op
```

The number of allocations is now consistent and small: just three or four for every buffer size. What is interesting is that you now can make trade-offs. If you are tight on memory, you can use a smaller buffer size and save memory at the expense of performance.

If benchmarking reveals that you have a performance or memory problem, the next step is figuring out exactly what the problem is. Go includes profiling tools that gather CPU and memory usage data from a running program as well as tools that help you visualize and interpret the generated data. You can even expose a web service endpoint to gather profiling information remotely from a running Go service. This data can even be used at compile time to improve performance automatically. I talk about instrumentating code and understanding profile data in Chapter 17.

### benchstat

How do you keep track of performance changes between versions of code and how do you know that the differences are significant? You could eyeball the output and try to remember, but it’s better to use benchstat, a tool built by the Go team that automates the process. Add benchstat to your Go module using:

```sh
go get -tool golang.org/x/perf/cmd/benchstat
```

When capturing benchmarks for benchstat, you need to run them multiple times and save the output to disk. The -count flag controls the number of times each benchmark runs; set it to 10 by default:

```sh
go test -bench=BenchmarkFileLen$ -count=10 -benchmem > base.txt
# move the allocation from inside the for loop to before the for loop
go test -bench=BenchmarkFileLen$ -count=10 -benchmem > new.txt
```

Compare the runs using go tool benchstat base.txt new.txt. Here are the results I obtained by running benchstat for benchmarks on last the two versions of the FileLen function:

```console
$ go tool benchstat base.txt new.txt
goos: darwin
goarch: arm64
pkg: github.com/learning-go-book-3e/ch15/sample_code/bench
cpu: Apple M3 Max
                             base.txt       new.txt    new.txt
                              sec/op        sec/op     vs base
FileLen/FileLen-1-16        23.83m ± 1%   23.80m ± 0%        ~ (p=0.796 n=10)
FileLen/FileLen-10-16       2.433m ± 1%   2.412m ± 0%   -0.85% (p=0.000 n=10)
FileLen/FileLen-100-16      263.3µ ± 2%   249.4µ ± 1%   -5.31% (p=0.000 n=10)
FileLen/FileLen-1000-16     38.93µ ± 1%   33.80µ ± 0%  -13.18% (p=0.000 n=10)
FileLen/FileLen-10000-16    16.13µ ± 2%   12.69µ ± 2%  -21.35% (p=0.000 n=10)
FileLen/FileLen-100000-16   19.02µ ± 2%   14.15µ ± 1%  -25.60% (p=0.000 n=10)
geomean                     238.1µ        210.5µ       -11.63%

                              base.txt         new.txt    new.txt
                                B/op            B/op      vs base
FileLen/FileLen-1-16           128.0 ± 0%     128.0 ± 0%        ~ (p=1.000 n=10) ¹
FileLen/FileLen-10-16          128.0 ± 0%     128.0 ± 0%        ~ (p=1.000 n=10) ¹
FileLen/FileLen-100-16       73040.0 ± 0%     240.0 ± 0%  -99.67% (p=0.000 n=10)
FileLen/FileLen-1000-16     66.125Ki ± 0%   1.125Ki ± 0%  -98.30% (p=0.000 n=10)
FileLen/FileLen-10000-16     80.12Ki ± 0%   10.12Ki ± 0%  -87.36% (p=0.000 n=10)
FileLen/FileLen-100000-16    208.1Ki ± 0%   104.1Ki ± 0%  -49.97% (p=0.000 n=10)
geomean                      10.35Ki        1.277Ki       -87.66%
¹ all samples are equal

                              base.txt      new.txt    new.txt
                             allocs/op     allocs/op   vs base
FileLen/FileLen-1-16          3.000 ± 0%   3.000 ± 0%        ~ (p=1.000 n=10) ¹
FileLen/FileLen-10-16         3.000 ± 0%   3.000 ± 0%        ~ (p=1.000 n=10) ¹
FileLen/FileLen-100-16      654.000 ± 0%   4.000 ± 0%  -99.39% (p=0.000 n=10)
FileLen/FileLen-1000-16      69.000 ± 0%   4.000 ± 0%  -94.20% (p=0.000 n=10)
FileLen/FileLen-10000-16     11.000 ± 0%   4.000 ± 0%  -63.64% (p=0.000 n=10)
FileLen/FileLen-100000-16     5.000 ± 0%   4.000 ± 0%  -20.00% (p=0.000 n=10)
geomean                       16.78        3.634       -78.34%
¹ all samples are equal
```

The first table shows the difference in CPU time, the second the difference in number of bytes allocated on the heap, and the third the difference in number of times the memory had to be allocated from the heap. Each of the numbers is given a variance range (such as ± 1%); lower is better. The p value ranges from 0 to 1, telling you the likelihood that the comparison is valid. Zero means you can trust the result, one means you can’t, and a number inbetween indicates the degree of trust. If the difference between the base case and the new case is not statistically significant, you will see a high value for p; feel free to ignore it. In other cases, a p value less than 0.05 is ideal.

If the variance or the p value is high, ensure that your computer wasn’t busy running other tasks while you were collecting benchmark data. You can also use the -count flag to increase the number of benchmark runs or the -benchtime flag to force each benchmark to run for a set number of seconds (-benchtime=2s for a two second run) or to run a set number of times (-benchtime=100000x to force each benchmark to run 100,000 times).

## Finding Concurrent Data Access Problems with the Data Race Detector

Even with Go’s built-in support for concurrency, bugs still happen. It’s easy to accidentally reference a variable from two different goroutines without acquiring a lock. The computer science term for this is a data race. To help find these sorts of bugs, Go includes a race detector. It isn’t guaranteed to find every single data race in your code, but if it finds one, you should put proper locks around what it finds.

Look at a simple example in the file `sample_code/race/race.go` in the Chapter 15 repository:

```go
func getCounter() int {
    var counter int
    var wg sync.WaitGroup
    for range 5 {
        wg.Go(func() {
            for range 1000 {
                counter++
            }
        })
    }
    wg.Wait()
    return counter
}
```

This code launches five goroutines, has each of them update a shared counter variable 1,000 times, and then returns the result. You’d expect it to be 5,000, so let’s verify this with a unit test in `sample_code/race/race_test.go`:

```go
func TestGetCounter(t *testing.T) {
    counter := getCounter()
    if counter != 5000 {
        t.Error("unexpected counter:", counter)
    }
}
```

If you run go test a few times, you’ll see that sometimes it passes, but most of the time it fails with an error message like this:

```text
unexpected counter: 3673
```

The problem is that there’s a data race in the code. In a program this simple, the cause is obvious: multiple goroutines are trying to update counter simultaneously, and some of their updates are lost. In more complicated programs, these sorts of races are harder to see. Let’s see what the data race detector does. Use the flag -race with go test to enable it:

```console
$ go test -race
==================
WARNING: DATA RACE
Read at 0x00c000128070 by goroutine 10:
  test_examples/race.getCounter.func1()
      test_examples/race/race.go:12 +0x45

Previous write at 0x00c000128070 by goroutine 8:
  test_examples/race.getCounter.func1()
      test_examples/race/race.go:12 +0x5b
```

The traces make it clear that the line counter++ is the source of your problems.

> **Warning**
>
> Some people try to fix race conditions by inserting “sleeps” into their code, trying to space out access to the variable that’s being accessed by multiple goroutines. This is a bad idea. Doing so might eliminate the problem in some cases, but the code is still wrong and will fail in some situations.

You can also use the -race flag when you build your programs. This creates a binary that includes the data race detector and that reports any races it finds to the console. This allows you to find data races in code that doesn’t have tests.

If the data race detector is so useful, why isn’t it enabled all the time for testing and production? A binary with -race enabled runs approximately 10 times slower than a normal binary. That isn’t a problem for test suites that take a second to run, but for large test suites that take several minutes, a 10× slowdown reduces productivity.

For more information on the data race detector, check out its official documentation.

## Test Concurrent Code with synctest

You might be surprised to discover that a language with strong support for both testing and concurrency did not initially include strong support for testing concurrency. The release of Go 1.25 addressed this oversight with the synctest package.

There are three common situations that were difficult to test before the release of synctest. First, there’s code that depends on time passing. Say that you implement a simple cache with expiration. You can put values into it and read values from it. If a value isn’t read within the expiration period, it is no longer returned by the cache.

```go
func (c *Cache[K, V]) Get(key K) (V, bool) {
    c.mu.Lock()
    defer c.mu.Unlock()
    e, ok := c.items[key]
    if !ok || time.Now().After(e.expiresAt) {
        delete(c.items, key)
        var zero V
        return zero, false
    }
    return e.value, true
}
```

This code gets a value from the cache. (The complete implementation is in the cachev1 directory in the Chapter 15 repository) It compares the time that an entry was placed into the cache against the current time. Being a good developer, you want to write a test to make sure this code functions correctly. Since the cache has different behavior depending on how much time has passed, you need to include `time.Sleep` calls to put pauses into reads and writes to the cache.

Here’s a test that puts a value into the cache, sleeps until the value expires, and then confirms that the value isn’t present:

```go
func TestCache_GetAfterExpiry_standard(t *testing.T) {
    c := cachev1.New[string, int](1 * time.Second)
    c.Set("answer", 42)

    // Jump past the TTL.
    time.Sleep(1100 * time.Millisecond)

    _, ok := c.Get("answer")
    if ok {
        t.Fatal("expected key to be expired after TTL")
    }
}
```

If you run this test, it passes, but that call to `time.Sleep` means it takes about a second to run. It’s only one second, but properly testing this cache requires additional tests that also require `time.Sleep` calls. Other parts of your program are liable to have their own tests that require the passage of time and this adds up. Unit tests should execute quickly to prevent developers from being distracted. That’s where synctest is useful.

The synctest package defines two functions: `synctest.Test` and `synctest.Wait`. I’ll talk about Test first. It has the signature:

```go
func Test(t *testing.T, f func(*testing.T))
```

This looks a lot like the `t.Run` method used in “Running Table Tests”. Like `t.Run`, `synctest.Test` creates a sub-environment. In the case of `synctest.Test`, this environment has magic powers. Each call to `synctest.Test` creates what the Go team calls a “bubble”. In this bubble, there is a fake clock, which starts at January 1st, 2000 UTC. Within the bubble, every `time.Sleep` call or use of a `time.Ticker` or `time.Timer` is tracked across all goroutines launched in the bubble. This allows the fake clock to move forward without waiting for the specified time to elapse in the real world.

An example makes this easier to understand. Say you have a test that looks like this:

```go
func TestTimeWaiting(t *testing.T) {
    start := time.Now() // real wall clock time/date
    go func() {
        time.Sleep(1 * time.Second)
        t.Log(time.Since(start)) // may not be exactly "1s"
        t.Log(time.Now())
    }()
    // the goroutine above will run before this Sleep returns
    time.Sleep(2 * time.Second)
    t.Log(time.Since(start))    // may not be exactly "2s"
    t.Log(time.Now())
}
```

Running this test takes 2 seconds to complete. But if you use `synctest.Test`, the test completes instantly:

```go
func TestTime(t *testing.T) {
    synctest.Test(t, func(t *testing.T) {
        start := time.Now() // always midnight UTC 2000-01-01
        go func() {
            time.Sleep(1 * time.Second)
            t.Log(time.Since(start)) // always logs "1s"
            t.Log(time.Now())
        }()
        // the goroutine above will run before this Sleep returns
        time.Sleep(2 * time.Second)
        t.Log(time.Since(start))    // always logs "2s"
        t.Log(time.Now())
    })
}
```

> **Note**
>
> synctest requires Go 1.25 or later. If you get an error like this, Check your `go.mod` file and update the specified version of Go:

```text
panic: synctest.Run not supported with asynctimerchan!=0
```

If we apply this pattern to the TestCache_GetAfterExpiry_standard function from earlier, running the test is now instanteous.

```go
func TestCache_GetAfterExpiry_synctest(t *testing.T) {
    synctest.Test(t, func(t *testing.T) {
        c := cachev1.New[string, int](1 * time.Second)
        c.Set("answer", 42)

        // Jump past the TTL.
        time.Sleep(1100 * time.Millisecond)

        _, ok := c.Get("answer")
        if ok {
            t.Fatal("expected key to be expired after TTL")
        }
    })
}
```

Using synctest also helps ensure that all goroutines properly exit. As mentioned in Chapter 12, you must make sure that every goroutine launched also exits. Let’s demonstrate this with an improved cache implementation. The first version doesn’t remove elements when they expire; it waits for them to be looked up again. This leaks memory if an entry is placed in the cache and never referenced again. Let’s add a background job to remove expired elements:

```go
func (c *Cache[K, V]) clean(interval time.Duration) {
    ticker := time.NewTicker(interval)
    defer ticker.Stop()
    for range ticker.C {
        c.mu.Lock()
        now := time.Now()
        for k, e := range c.items {
            if now.After(e.expiresAt) {
                delete(c.items, k)
                c.Stats.RemovedBySweep++
            }
        }
        c.mu.Unlock()
    }
}

func New[K comparable, V any](ttl, sweepInterval time.Duration) *Cache[K, V] {
    c := &Cache[K, V]{
        items: make(map[K]entry[V]),
        ttl:   ttl,
        done:  make(chan struct{}),
    }
    go c.clean(sweepInterval)
    return c
}
```

Every time you create a new cache instance with the New function, it also launches a goroutine to remove any items that have already expired. (The rest of the code for this cache implementation is in the cachev2 directory in the Chapter 15 repository.) Again, being a good developer, you write a test to validate that this code works. The implementation tracks how many entries are removed via clean, so you can check this value:

```go
func TestCache_Clean(t *testing.T) {
    c := cachev2.New[string, string](2*time.Second, 1*time.Second)
    c.Set("key", "hello")
    time.Sleep(4 * time.Second)
    val, ok = c.Get("key")
    if ok {
        t.Fatal("expected key to not be present")
    }
    if c.Stats.RemovedByClean != 1 {
        t.Error("expected removed by Sweep to be 1")
    }
}
```

If you run this test, it will pass, but it takes 4 seconds for the test to complete. Wrapping it in `synctest.Test` to speed up the test produces a surprising result:

```text
=== RUN   TestCache_Clean_synctest
--- FAIL: TestCache_Clean_synctest (0.00s)
panic: deadlock: main bubble goroutine has exited but blocked
    goroutines remain [recovered, repanicked]
...
```

The synctest bubble ensures that every goroutine created within the bubble exits before the bubble ends. (I wish the Go team had called this “popping”, but the software industry is not in a whimsical moment.) If any goroutines continue to run, the test panics. Looking at the implemmentation of clean, there’s no way to signal to the goroutine when to exit. Without synctest, problems like this are very hard to detect.

The following changes fix this. First we update our cache implementation:

```go
func (c *Cache[K, V]) clean(interval time.Duration) {
    ticker := time.NewTicker(interval)
    defer ticker.Stop()
    for {
        select {
        case <-ticker.C:
            c.mu.Lock()
            now := time.Now()
            for k, e := range c.items {
                if !now.Before(e.expiresAt) {
                    delete(c.items, k)
                    c.Stats.RemovedBySweep++
                }
            }
            c.mu.Unlock()
        case <-c.done:
            return
        }
    }
}

func (c *Cache[K, V]) Done() {
    c.mu.Lock()
    defer c.mu.Unlock()
    select {
    case <-c.done:
        return
    default:
        close(c.done)
    }
}
```

Next, we fix the test to call c.Done:

```go
func TestCache_Clean_synctest(t *testing.T) {
    synctest.Test(t, func(t *testing.T) {
        c := cachev2.New[string, string](2*time.Second, 1*time.Second)
        t.Cleanup(c.Done)
        c.Set("key", "hello")
        time.Sleep(4 * time.Second)
        synctest.Wait()
        val, ok = c.Get("key")
        if ok {
            t.Error("expected key to not be present")
        }
        if c.Stats.RemovedBySweep != 1 {
            t.Error("expected removed by Sweep to be 1")
        }
    })
}
```

With the new clean implementation and the addition of the Done method, the test passes when it includes a call to `t.Cleanup`(c.Done).

This brings us to the third problem addressed by synctest. You might have noticed the call to `synctest.Wait`() in the fixed code and wondered what it does. Before I answer that question, think about this: how do you know that sleeping for 4 seconds is enough? You know that the background cleaner goroutine will receive a tick from its timer within 4 seconds, but how do you know that it will finish looking for expired cache entries to remove and get back to waiting for the next tick of its timer?

The fact is that you don’t know how long to wait; you are taking for granted that it should be enough time. If you write tests this way and run them on a machine with lots of load (like a shared CI/CD server), you might find enough isn’t enough. Unless you use an absurdly big value for `time.Sleep`, tests fail randomly. In a synctest bubble where time “passes” instanteously, it becomes more likely that the work won’t complete.

The `synctest.Wait` function provides a solution for this problem. When you call it from inside a closure that’s passed to `synctest.Test`, the test pauses until all other goroutines run to completion, are waiting to read from or write to a channel, sleeping with a `time.Sleep`, waiting on a WaitGroup.Wait, or waiting on a Cond.Wait. The synctest spec calls this being “durably blocked”.

To make our background cleaner test correct, we need to add a `synctest.Wait` call after the `time.Sleep`(4 * `time.Second`). This guarantees that the clean goroutine not only gets a chance to run, but that it runs until it is waiting to read the next tick from the ticker channel. This ensures that the entry was removed from the cache.

The synctest package solves many of the problems in testing concurrent code, but it does have some limitations. For more details, look at the package documentation and the blog post from the Go team that introduced synctest.

## Code Review: Advanced Testing

- Code coverage is necessary, but not sufficient. Even code with 100% code coverage can contain bugs. Make sure that tests include multiple sets of data for the same paths through the code. And always test inputs that should produce errors.

- If your program processes data you don’t control (and most programs do), include fuzzing tests in your test suites.

- Don’t guess that your changes made the code faster---measure. Capture benchmarks and use Benchstat to track improvements and regressions over time.

- When testing concurrent code, use the data race detector to ensure you aren’t accessing shared data without locks and use synctest to make the tests fast and accurate.

## Exercises

Now that you’ve seen the more advanced testing tools provided by Go, these exercises will give you a chance to try them out. They are found in the exercises directory in the Chapter 15 repository. Solutions are in the `exercise-solutions` directory in the Chapter 15 repository.

1. In the ex4 directory, there is a file called wealth.go with a function called CalcWealth and a test for this function in the file `wealth_test.go`. Check the code coverage from this test. Examine the code and see if there’s a bug that wasn’t detected by the test. If so, add a test to demonstrate the bug, then fix the code.

2. In the ex5 directory, there is a file called count.go. It contains three functions that perform the same task, CountWithFields, CountWithFieldsSeq, and CountManual. Write tests to validate that these functions work, then write benchmarks to compare their performance and amount of memory used.

3. In the ex6 directory, there is a file called tracker.go with a type called Tracker. There is a test for this function in `tracker_test.go`. See if the test passes. If it does not, use the data race detector to figure out why, and fix the code to make it pass. Hint: fixing a concurrent bug might require you to think about lock acquisition and release lifetimes.

## Using Stubs in Go

So far, you’ve written tests for functions that didn’t depend on other code. This is not typical, as most code is filled with dependencies. As you saw in Chapter 7, Go allows you to abstract function calls in two ways: defining a function type and defining an interface. These abstractions help you write not only modular production code but also unit tests that take advantage of stubs, which are code used during testing to return a specific value for a given input.

> **Tip**
>
> When your code depends on abstractions, it’s easier to write unit tests!

Let’s take a look at an example in the `sample_code/solver` directory in the Chapter 15 repository. Define a type called Processor:

```go
type Processor struct {
    Solver MathSolver
}
```

It has a field of type MathSolver:

```go
type MathSolver interface {
    Resolve(ctx context.Context, expression string) (float64, error)
}
```

You’ll implement and test MathSolver in a bit.

Processor also has a method that reads an expression from an `io.Reader` and returns the calculated value:

```go
func (p Processor) ProcessExpression(ctx context.Context, r io.Reader)
                                    (float64, error) {
    curExpression, err := readToNewLine(r)
    if err != nil {
        return 0, err
    }
    if len(curExpression) == 0 {
        return 0, ErrNoExpression
    }
    answer, err := p.Solver.Resolve(ctx, curExpression)
    return answer, err
}
```

Let’s write the code to test ProcessExpression. First, you need a stub implementation of the Resolve method to write your test:

```go
type mathSolverStub struct{}

func (ms mathSolverStub) Resolve(ctx context.Context, expr string)
                                (float64, error) {
    switch expr {
    case "2 + 2 * 10":
        return 22, nil
    case "( 2 + 2 ) * 10":
        return 40, nil
    case "( 2 + 2 * 10":
        return 0, &InvalidExpressionErr{Expression: "( 2 + 2 * 10"}
    }
    return 0, nil
}
```

Next, you write a unit test that uses this stub:

```go
func TestProcessor_ProcessExpressions(t *testing.T) {
    p := Processor{mathSolverStub{}}
    in := strings.NewReader(`2 + 2 * 10
( 2 + 2 ) * 10
( 2 + 2 * 10`)
    data := []struct {
        name string
        val  float64
        err  error
    }{
        {name: "case1", val: 22, err: nil},
        {name: "case2", val: 40, err: nil},
        {name: "case3", val: 0,
         err: &InvalidExpressionErr{Expression: "( 2 + 2 * 10"}},
    }
    for _, d := range data {
        t.Run(d.name, func(t *testing.T) {
            result, err := p.ProcessExpression(t.Context(), in)
            if !errors.Is(err, d.err) {
                t.Errorf("expected error %v, got %v", d.err, err)
            }
            if result != d.val {
                t.Errorf("Expected result %f, got %f", d.val, result)
            }
        })
    }
}
```

You can then run your test and see that everything works.

While most Go interfaces specify only one or two methods, you’ll sometimes find yourself with an interface that has many methods. Let’s take a look at the code in the `sample_code/stub` directory in the Chapter 15 repository. Assume you have an interface that looks like this:

```go
type Entities interface {
    GetUser(id string) (User, error)
    GetPets(userID string) ([]Pet, error)
    GetChildren(userID string) ([]Person, error)
    GetFriends(userID string) ([]Person, error)
    SaveUser(user User) error
}
```

There are two patterns for testing code that depends on large interfaces. The first is to embed the interface in a struct, which automatically defines all the interface’s methods on the struct. It doesn’t provide any implementations of those methods, so you need to implement the methods that you care about for the current test. Let’s assume that Logic is a struct that has a field of type Entities:

```go
type Logic struct {
    Entities Entities
}
```

Assume you want to test this method:

```go
func (l Logic) GetPetNames(userId string) ([]string, error) {
    pets, err := l.Entities.GetPets(userId)
    if err != nil {
        return nil, err
    }
    out := make([]string, len(pets))
    for _, p := range pets {
        out = append(out, p.Name)
    }
    return out, nil
}
```

This method only uses the GetPets method declared on Entities. Rather than creating a stub that implements every single method on Entities just to test GetPets, you can write a stub struct that implements only the method you need to test this method:

```go
type getPetNamesStub struct {
    Entities
}

func (ps getPetNamesStub) GetPets(userID string) ([]Pet, error) {
    switch userID {
    case "1":
        return []Pet{{Name: "Bubbles"}}, nil
    case "2":
        return []Pet{{Name: "Stampy"}, {Name: "Snowball II"}}, nil
    default:
        return nil, &InvalidIDError{ID: userID}
    }
}
```

You then write your unit test, with your stub injected into Logic:

```go
func TestLogicGetPetNames(t *testing.T) {
    data := []struct {
        name     string
        userID   string
        petNames []string
        err      error
    }{
        {"case1", "1", []string{"Bubbles"}, nil},
        {"case2", "2", []string{"Stampy", "Snowball II"}, nil},
        {"case3", "3", nil, &InvalidIDError{ID: "3"}},
    }
    l := Logic{getPetNamesStub{}}
    for _, d := range data {
        t.Run(d.name, func(t *testing.T) {
            petNames, err := l.GetPetNames(d.userID)
            if !errors.Is(err, d.err) {
                t.Errorf("expected error %v, got %v", d.err, err)
            }
            if diff := cmp.Diff(d.petNames, petNames); diff != "" {
                t.Error(diff)
            }
        })
    }
}
```

(By the way, the GetPetNames method has a bug. Did you see it? Even simple methods can sometimes have bugs.)

> **Warning**
>
> If you embed an interface in a stub struct, make sure you provide an implementation for every method that’s called during your test! If you call an unimplemented method, your tests will panic.

If you need to implement only one or two methods in an interface for a single test, this technique works well. The drawback comes when you need to call the same method in different tests with different inputs and outputs. When that happens, you need to either include every possible result for every test within the same implementation or reimplement the struct for each test. This quickly becomes difficult to understand and maintain. A better solution is to create a stub struct that proxies method calls to function fields. For each method defined on Entities, define a function field with a matching signature on your stub struct:

```go
type entitiesStub struct {
    getUser     func(id string) (User, error)
    getPets     func(userID string) ([]Pet, error)
    getChildren func(userID string) ([]Person, error)
    getFriends  func(userID string) ([]Person, error)
    saveUser    func(user User) error
}
```

Then make entitiesStub meet the Entities interface by defining the methods. In each method, invoke the associated function field. For example:

```go
func (es entitiesStub) GetUser(id string) (User, error) {
    return es.getUser(id)
}

func (es entitiesStub) GetPets(userID string) ([]Pet, error) {
    return es.getPets(userID)
}
```

Once you create this stub, you can supply different implementations of different methods in different test cases via the fields in the data struct for a table test:

```go
func TestLogicGetPetNames2(t *testing.T) {
	data := []struct {
		name     string
		getPets  func(userID string) ([]Pet, error)
		userID   string
		petNames []string
		err      error
	}{
		{"case1", func(userID string) ([]Pet, error) {
			return []Pet{{Name: "Bubbles"}}, nil
		}, "1", []string{"Bubbles"}, nil},
		{"case2", func(userID string) ([]Pet, error) {
			return []Pet{{Name: "Stampy"}, {Name: "Snowball II"}}, nil
		}, "2", []string{"Stampy", "Snowball II"}, nil},
		{"case3", func(userID string) ([]Pet, error) {
			return nil, &InvalidIDError{ID: "3"}
		}, "3", nil, &InvalidIDError{ID: "3"}},
	}
	for _, d := range data {
		t.Run(d.name, func(t *testing.T) {
			l := Logic{Entities: entitiesStub{getPets: d.getPets}}
			petNames, err := l.GetPetNames(d.userID)
			if diff := cmp.Diff(d.petNames, petNames); diff != "" {
				t.Error(diff)
			}
			if !errors.Is(err, d.err) {
				t.Errorf("Expected error %v, got %v", d.err, err)
			}
		})
	}
}
```

Add a field of function type to data’s anonymous struct. In each test case, specify a function that returns the data that GetPets would return. When you write your test stubs this way, it’s clear what the stubs should return for each test case. Each test run instantiates a new EntitiesStub and assigns the getPets function field in the test data to the getPets function field in EntitiesStub.

### Mocks and Stubs

The terms mock and stub are often used interchangeably, but they are actually two different concepts. Martin Fowler, a respected voice on all things related to software development, wrote a blog post on mocks that, among other things, covers the difference. In short, a stub returns a canned value for a given input, whereas a mock validates that a set of calls happen in the expected order with the expected inputs.

You used stubs in the examples to return canned values to a given response. You can write your own mocks by hand, or you can use a third-party library to generate them. The two most popular options are the gomock library from Google and the testify library from Stretchr, Inc.

### Using httptest

It’s important to ensure that calls to HTTP services send the right requests and handle responses properly. While integration testing is essential for validating a multi-service deployment, it is often slow. Quick-running unit tests for HTTP clients provide confidence during development. The Go standard library includes the net/http/httptest package, which makes it easy to stub HTTP services. Let’s go back to the `sample_code/solver` directory in the Chapter 15 repository and provide an implementation of MathSolver that calls an HTTP service to evaluate expressions:

```go
type RemoteSolver struct {
    MathServerURL string
    Client        *http.Client
}

func (rs RemoteSolver) Resolve(ctx context.Context, expression string)
                              (float64, error) {
    req, err := http.NewRequestWithContext(ctx, http.MethodGet,
        rs.MathServerURL+"?expression="+url.QueryEscape(expression), nil)
    if err != nil {
        return 0, err
    }
    resp, err := rs.Client.Do(req)
    if err != nil {
        return 0, err
    }
    defer resp.Body.Close()
    contents, err := io.ReadAll(resp.Body)
    if err != nil {
        return 0, err
    }
    if resp.StatusCode != http.StatusOK {
        return 0, &RequestErr{
            StatusCode: resp.StatusCode,
            Contents:   string(contents),
        }
    }
    result, err := strconv.ParseFloat(string(contents), 64)
    if err != nil {
        return 0, err
    }
    return result, nil
}
```

Now let’s see how to use the httptest library to test this code without standing up a server. The code is in the TestRemoteSolver_Resolve function in `sample_code/solver/remote_solver_test.go` in the Chapter 15 repository, but here are the highlights. First, you want to make sure that the data that’s passed into the function arrives on the server. In your test function, define a type called info to hold your input and output and a variable called io that is assigned the current input and output:

```go
type info struct {
    expression string
    code       int
    body       string
}
var io info
```

Next, set up your fake remote server and use it to configure an instance of RemoteSolver:

```go
server := httptest.NewServer(
    http.HandlerFunc(func(rw http.ResponseWriter, req *http.Request) {
        // validate the incoming request to make sure the client is
        // sending the expected data
        if req.URL.Query().Get("expression") != io.expression {
            rw.WriteHeader(http.StatusBadRequest)
            return
        }
        rw.WriteHeader(io.code)
        rw.Write([]byte(io.body))
    }))
defer server.Close()
rs := RemoteSolver{
    MathServerURL: server.URL,
    Client:        server.Client(),
}
```

The `httptest.NewServer` function creates and starts an HTTP server on a random unused port. You need to provide an `http.Handler` implementation to process the request. Since this is a server, you must close it when the test completes. The server instance has its URL specified in the URL field of the server instance and a preconfigured `http.Client` for communicating with the test server. Pass these into RemoteSolver.

The rest of the function works like every other table test that you’ve seen:

```go
data := []struct {
    name   string
    io     info
    result float64
    err    error
}{
    {"case1", info{"2 + 2 * 10", http.StatusOK, "22"}, 22, nil},
    {"case2", info{"( 2 + 2 ) * 10", http.StatusOK, "40"}, 40, nil},
    {"case3", info{"( 2 + 2 * 10", http.StatusBadRequest,
                    "invalid expression: ( 2 + 2 * 10"}, 0,
        &RequestErr{
            StatusCode: http.StatusBadRequest,
            Contents:   "invalid expression: ( 2 + 2 * 10",
        }},
}
for _, d := range data {
    t.Run(d.name, func(t *testing.T) {
        io = d.io
        result, err := rs.Resolve(t.Context(), d.io.expression)
        if result != d.result {
            t.Errorf("io `%f`, got `%f`", d.result, result)
        }
        if !errors.Is(err, d.err) {
            t.Errorf("expected error %v, got %v", d.err, err)
        }
    })
}
```

The variable io has been captured by two closures: the one for the stub server and the one for running each test. You write to it in one closure and read it in the other. This is a bad idea in production code, but it works well in test code within a single function.

## Using Integration Tests and Build Tags

Even though httptest provides a way to avoid testing against external services, you should still write integration tests, automated tests that connect to other services. These validate that your understanding of the service’s API is correct. The challenge is figuring out how to group your automated tests; you want to run integration tests only when the support environment is present. Also, integration tests tend to be slower than unit tests, so they are usually run less frequently.

In Chapter 11, I covered build tags, which the Go compiler uses to control when a file is compiled. While they are primarily intended to allow developers to write code that’s intended only for a specific operating system, CPU, or Go version, you can take advantage of the ability to specify custom build tags to control when integration tests are compiled and run.

Let’s try this out with the math-solving project. Use Docker to download a server implementation with docker pull jonbodner/math-server and then run the server locally on port 8080 with docker run -p 8080:8080 jonbodner/math-server. (The `sample_code/solver` directory in the Chapter 15 repository has a Docker Compose file, so if you have cloned it locally, you can run docker compose up.)

> **Note**
>
> If you don’t have Docker installed or if you want to build the code for yourself, you can find the math-server code on GitHub.

You need to write an integration test to make sure that your Resolve method properly communicates with the math server. The `sample_code/solver/remote_solver_integration_test.go` file in the Chapter 15 repository has a complete test in the TestRemoteSolver_ResolveIntegration function. The test looks like every other table test that you’ve written. The interesting thing is the first line of the file, separated from the package declaration by a newline:

```go
//go:build integration
```

To run your integration test alongside the other tests you’ve written, use this:

```console
$ go test -tags integration -v ./...
```

Some people in the Go community prefer to use environment variables rather than build tags to create groups of integration tests. Peter Bourgon describes the concept in a blog post with the unsubtle title “Don’t Use Build Tags for Integration Tests”. His argument is that it’s hard to find out what build tags to set in order to run integration tests. An explicit check for an environment variable in each integration test, combined with a detailed message in a `t.Skip` method call, makes it clear that tests aren’t being run and how to run them. The downside to this approach is that it is far more verbose than using a build tag, since it requires the developer to include a preamble in every integration test.

Yet another way to group tests is to use go test with the -short flag. If you want to skip over tests that take a long time, label your slow tests by placing the following code at the start of the test function:

```go
if testing.Short() {
    t.Skip("skipping test in short mode.")
}
```

When you want to run only short tests, pass the -short flag to go test.

There are a few problems with the -short flag. It has the same verbosity problem as using environment variables, but doesn’t give you any flexibility for grouping your tests, since it only allows for two levels of testing: short tests and all tests. Both build tags and environment variables let you group your integration tests, specifying which services should run. Another argument against using the -short flag to indicate integration tests is philosophical: build tags indicate a dependency, while the -short flag is meant to indicate only that you don’t want to run tests that take a long time. Those are different concepts. Finally, I find the -short flag unintuitive. You should run short tests all the time. It makes more sense to require a flag to include long-running tests, not to exclude them.

## Code Review: Tests with Mocks and Stubs

- Make sure your code interacts with other components via abstractions. They make code easier to understand and easier to test.

- Prefer function-field stubs over switch-statement stubs when the same method needs different behavior across test cases.

- Stubs are useful for testing, but verify that usign one is helping you test your production code, not the stub itself.

- Use httptest to validate that the HTTP clients in your code are both sending and receiving data correctly.

- Separate unit tests from integration test via tags or environment variables.

## Exercises

Now that you’ve learned about using mocks and stubs, complete these exercises to apply that knowledge to a sample application.

1. In the ex7 directory, the notifier.go file contains a type called NotificationService with a method called Notify. Use a function field stub to write a table test to make sure this code properly handles correct data, invalid input, and a failed send.

2. In the ex8 directory, the report.go file contains a type called ReportBuilder with a method called PriceSummary. ReportBuilder depends on a large interface (DataStore), but PriceSummary only used one method in the interface. Write a test to validate that PriceSummary works correctly.

3. In the ex9 directory, the weather.go file contains a type called Client with a method called GetTemperature, which connects to a remote HTTP server to get weather data. Write a unit test to validate this method that doesn’t require you to run an external server.

## Wrapping Up

In this chapter, you’ve learned how to write tests and improve code quality by using Go’s built-in support for testing, code coverage, benchmarking, fuzzing, and data race checking. In the next chapter, you’re going to explore some Go features that allow you to break the rules: the unsafe package, reflection, and cgo.
